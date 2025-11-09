from selenium.webdriver.common.by import By

"""Зробив у форматі классів, так як відразу запускав і перевіряв що знаходить локатори"""

"""хедер сторінки https://qauto2.forstudy.space/
таби під якір, кнопка гостьвого логіну, кнопка на форму логіну """


class MainPageHeaderLocators:
    def __init__(self):
        self.home_tab_xpath = (By.XPATH, "//a[text()='Home']")
        self.home_tab_css = (By.CSS_SELECTOR, ".btn.header-link.-active")

        self.about_tab_xpath = (By.XPATH, "//button[text()='About']")
        self.about_tab_css = (By.CSS_SELECTOR, "button[appscrollto='aboutSection']")

        self.contacts_tab_xpath = (By.XPATH, "//button[text()='Contacts']")
        self.contacts_tab_css = (By.CSS_SELECTOR, "button[appscrollto='contactsSection']")

        self.guest_login_xpath = (By.XPATH, "//button[text()='Guest log in']")
        self.guest_login_css = (By.CSS_SELECTOR, ".header-link.-guest")

        self.sign_in_button_xpath = (By.XPATH, "//button[normalize-space()='Sign In']")
        self.sign_in_button_css = (By.CSS_SELECTOR, ".btn.btn-outline-white.header_signin")


"""Частина сторінки із відео"""


class MainPage:
    def __init__(self):
        self.sign_up_button_xpath = (By.XPATH, "//button[text()='Sign up']")
        self.sign_up_button_css = (By.CSS_SELECTOR, ".hero-descriptor_btn.btn.btn-primary")


"""футер сторінки із посиланнями на соц.мережі та відправку емейлу в саппорт"""


class MainPageFooterLocators:
    def __init__(self):
        self.contacts_facebook_xpath = (By.XPATH, "//span[@class='socials_icon icon icon-facebook']")
        self.contacts_facebook_css = (By.CSS_SELECTOR, ".socials_icon.icon.icon-facebook")

        self.contacts_telegram_xpath = (By.XPATH, "//span[@class='socials_icon icon icon-telegram']")
        self.contacts_telegram_css = (By.CSS_SELECTOR, ".socials_icon.icon.icon-telegram")

        self.contacts_youtube_xpath = (By.XPATH, "//span[@class='socials_icon icon icon-youtube']")
        self.contacts_youtube_css = (By.CSS_SELECTOR, ".socials_icon.icon.icon-youtube")

        self.contacts_instagram_xpath = (By.XPATH, "//span[@class='socials_icon icon icon-instagram']")
        self.contacts_instagram_css = (By.CSS_SELECTOR, ".socials_icon.icon.icon-instagram")

        self.contacts_linkedin_xpath = (By.XPATH, "//span[@class='socials_icon icon icon-linkedin']")
        self.contacts_linkedin_css = (By.CSS_SELECTOR, ".socials_icon.icon.icon-linkedin")

        self.hillel_link_xpath = (By.XPATH, "//a[text()='ithillel.ua']")
        self.hillel_link_css = (By.CSS_SELECTOR, ".contacts_link.display-4")

        self.mail_support_link_xpath = (By.XPATH, "//a[text()='support@ithillel.ua']")
        self.mail_support_link_css = (By.CSS_SELECTOR, ".contacts_link.h4")


"""Форма логіну"""


class SignInForm:
    def __init__(self):
        self.email_input_xpath = (By.XPATH, "//input[@id='signinEmail']")
        self.email_input_css = (By.CSS_SELECTOR, "#signinEmail")
        self.email_required_validate_message_xpath = (By.XPATH, "//p[text()='Email required']")
        self.email_required_validate_message_css = (By.CSS_SELECTOR, "div.invalid-feedback:nth-of-type(1) p")
        self.email_incorrect_validation_message_xpath = (By.XPATH, "//p[text()='Email is incorrect']")
        self.email_incorrect_validation_message_css = (By.CSS_SELECTOR, "div.invalid-feedback:nth-of-type(1) p")

        self.password_input_xpath = (By.XPATH, "//input[@id='signinPassword']")
        self.password_input_css = (By.CSS_SELECTOR, "#signinPassword")
        self.password_required_validate_message_xpath = (By.XPATH, "//p[text()='Password required']")
        self.password_required_validate_message_css = (By.CSS_SELECTOR, "div.invalid-feedback:nth-of-type(2) p")

        self.remember_me_checkbox_xpath = (By.XPATH, "//input[@id='remember']")
        self.remember_me_checkbox_css = (By.CSS_SELECTOR, "#remember")

        self.forgot_password_xpath = (By.XPATH, "//button[text()='Forgot password']")
        self.forgot_password_css = (By.CSS_SELECTOR,
            "div[class='form-group d-flex align-items-center justify-content-between'] button[class='btn btn-link']")

        self.form_registration_xpath = (By.XPATH, "//button[text()='Registration']")
        self.form_registration_css = (By.CSS_SELECTOR,
                                      "div[class='modal-footer d-flex justify-content-between'] button:nth-child(1)")

        self.login_button_xpath = (By.XPATH, "//button[text()='Login']")
        self.login_button_css = (By.CSS_SELECTOR, "button[class='btn btn-primary']")


"""Форма регістрації"""


class RegistrationForm:
    def __init__(self):
        self.sign_up_name_input_xpath = (By.XPATH, "//input[@id='signupName']")
        self.sign_up_name_input_css = (By.CSS_SELECTOR, "#signupName")

        self.sign_up_last_name_input_xpath = (By.XPATH, "//input[@id='signupLastName']")
        self.sign_up_last_name_input_css = (By.CSS_SELECTOR, "#signupLastName")

        self.sign_up_email_input_xpath = (By.XPATH, "//input[@id='signupEmail']")
        self.sign_up_email_input_css = (By.CSS_SELECTOR, "#signupEmail")
        self.sign_up_email_required_validate_message_xpath = (By.XPATH, "//p[text()='Email required']")
        self.sign_up_email_required_validate_message_css = (By.CSS_SELECTOR, "div.invalid-feedback:nth-of-type(1) p")
        self.sign_up_email_incorrect_validate_message_xpath = (By.XPATH, "//p[text()='Email is incorrect']")
        self.sign_up_email_incorrect_validate_message_css = (By.CSS_SELECTOR, "div.invalid-feedback:nth-of-type(1) p")

        self.sign_up_password_input_xpath = (By.XPATH, "//input[@id='signupPassword']")
        self.sign_up_password_input_css = (By.CSS_SELECTOR, "#signupPassword")
        self.sign_up_password_required_validation_message_xpath = (By.XPATH, "//p[text()='Password required']")
        self.sign_up_password_required_validation_message_css = (By.CSS_SELECTOR,
                                                                 "#signupPassword + .invalid-feedback p")

        self.sign_up_re_password_input_xpath = (By.XPATH, "//input[@id='signupRepeatPassword']")
        self.sign_up_re_password_input_css = (By.CSS_SELECTOR, "#signupRepeatPassword")
        self.sign_up_re_password_required_validation_message_xpath = (By.XPATH,
                                                                      "//p[text()='Re-enter password required']")
        self.sign_up_re_password_required_validation_message_css = (By.CSS_SELECTOR,
                                                                    "#signupRepeatPassword + .invalid-feedback p")

        self.register_button_xpath = (By.XPATH, "//div[@class='modal-footer']/button[text()='Register']")
        self.register_button_css = (By.CSS_SELECTOR, ".modal-footer .btn-primary")

