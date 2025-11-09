from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
frames = [
    ("frame1", "input1", "Frame1_Secret"),
    ("frame2", "input2", "Frame2_Secret")
]
wait = WebDriverWait(driver, 5)

driver.get("http://localhost:8000/dz.html")

for frame_id, input_id, secret_text in frames:
    driver.switch_to.frame(frame_id)

    driver.find_element(By.ID, input_id).send_keys(secret_text)
    driver.find_element(By.XPATH, "//button[contains(text(),'Перевірити')]").click()

    alert = wait.until(EC.alert_is_present())
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()

    driver.switch_to.default_content()
driver.quit()