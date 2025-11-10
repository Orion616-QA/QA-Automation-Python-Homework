import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

wait = WebDriverWait

class TrackingSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.package_search_input = (By.XPATH, "//input[@id='en']")
        self.package_search_button = (By.CSS_SELECTOR, "#np-number-input-desktop-btn-search-en")
        self.context_button_good = (By.XPATH, "//button[@class='button v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default']")
        self.package_status_result = (By.CSS_SELECTOR, ".header__status-text")

    def open(self):
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

    def start_search_package(self, package_number):
        """Знаходить інпут, вводить номер посилки, виконує пошук"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.package_search_input)
        ).send_keys(package_number)

        self.driver.find_element(*self.package_search_button).click()

    def receive_package_status(self) -> str:
        """Попередньо перевірка вспливаючого контекстного вікна.
        Потім повертає текст результату пошуку"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.context_button_good)
            ).click()
        except:
            raise AttributeError

        status_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.package_status_result)
        )
        return status_element.text


def test_check_received_package_status(driver):
    page = TrackingSearchPage(driver)
    page.open()
    page.start_search_package("""Ввести номер вже отриманої посилки""")

    actual = page.receive_package_status()
    expected = "Отримана"

    assert actual == expected