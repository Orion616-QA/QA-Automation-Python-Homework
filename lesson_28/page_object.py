from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self):
        self.sign_up_button_xpath = (By.XPATH, "//button[text()='Sign up']")

class RegistrationForm:
    def __init__(self):
        self.sign_up_name_input_xpath = (By.XPATH, "//input[@id='signupName']")
        self.sign_up_last_name_input_xpath = (By.XPATH, "//input[@id='signupLastName']")
        self.sign_up_email_input_xpath = (By.XPATH, "//input[@id='signupEmail']")
        self.sign_up_password_input_xpath = (By.XPATH, "//input[@id='signupPassword']")
        self.sign_up_re_password_input_xpath = (By.XPATH, "//input[@id='signupRepeatPassword']")
        self.register_button_xpath = (By.XPATH, "//div[@class='modal-footer']/button[text()='Register']")
        self.success_register = (By.XPATH, "//p[text()='You don’t have any cars in your garage']")
        self.error_already_exist = (By.XPATH, "//p[text()='User already exists']")