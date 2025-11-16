import pytest
from playwright.sync_api import expect
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid
from page_object import MainPage, RegistrationForm


# Fixtures---------------------------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page():
    return MainPage()


@pytest.fixture
def registration_form():
    return RegistrationForm()


@pytest.fixture
def valid_user_data():
    """Створює дані із унікальним емейлом для регістрації"""
    unique = uuid.uuid4().hex[:8]
    return {
        "name": "Test",
        "last": "User",
        "email": f"user_{unique}@example.com",
        "password": "Qwerty123!"
    }


@pytest.fixture
def already_exist_user_data():
    """Дані вже зареєстрованого користувача"""
    return {
        "name": "Test",
        "last": "User",
        "email": "test@example.com",
        "password": "Qwerty123!"
    }


@pytest.fixture
def open_main_page(driver):
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

    return driver


@pytest.fixture
def valid_registration(open_main_page, main_page, registration_form, valid_user_data):
    """Відкриває форму реєстрації. Вводить валідні дані та виконує процесс реєстрації"""
    driver = open_main_page

    driver.find_element(*main_page.sign_up_button_xpath).click()

    driver.find_element(*registration_form.sign_up_name_input_xpath).send_keys(valid_user_data["name"])
    driver.find_element(*registration_form.sign_up_last_name_input_xpath).send_keys(valid_user_data["last"])
    driver.find_element(*registration_form.sign_up_email_input_xpath).send_keys(valid_user_data["email"])
    driver.find_element(*registration_form.sign_up_password_input_xpath).send_keys(valid_user_data["password"])
    driver.find_element(*registration_form.sign_up_re_password_input_xpath).send_keys(valid_user_data["password"])

    driver.find_element(*registration_form.register_button_xpath).click()

    return driver


@pytest.fixture
def invalid_registration(open_main_page, main_page, registration_form, already_exist_user_data):
    """Відкриває форму реєстрації. Вводить дані вже зареєстрованого юзера та виконує процесс реєстрації"""
    driver = open_main_page

    driver.find_element(*main_page.sign_up_button_xpath).click()

    driver.find_element(*registration_form.sign_up_name_input_xpath).send_keys(already_exist_user_data["name"])
    driver.find_element(*registration_form.sign_up_last_name_input_xpath).send_keys(already_exist_user_data["last"])
    driver.find_element(*registration_form.sign_up_email_input_xpath).send_keys(already_exist_user_data["email"])
    driver.find_element(*registration_form.sign_up_password_input_xpath).send_keys(already_exist_user_data["password"])
    driver.find_element(*registration_form.sign_up_re_password_input_xpath).send_keys(
        already_exist_user_data["password"])

    driver.find_element(*registration_form.register_button_xpath).click()

    return driver


# Tests------------------------------------------------
def test_valid_registration(valid_registration, registration_form):
    driver = valid_registration

    expected = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(registration_form.success_register)
    )

    assert expected.is_displayed(), "Process register not success"


def test_error_user_already_exist(invalid_registration, registration_form):
    driver = invalid_registration
    expected = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(registration_form.error_already_exist)
    )

    assert expected.is_displayed(), "Process test not such as expected"