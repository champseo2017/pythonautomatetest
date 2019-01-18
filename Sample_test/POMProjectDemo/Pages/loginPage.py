from Sample_test.POMProjectDemo.Locators.locators import Locators #import locators
class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.email_emailbox_id = Locators.email_emailbox_id
        self.password_passwordbox_id = Locators.password_passwordbox_id
        self.login_button_id = Locators.login_button_id
        self.login_in_valid = Locators.login_in_valid

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_emailbox_id).clear()
        self.driver.find_element_by_id(Locators.email_emailbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_passwordbox_id).clear()
        self.driver.find_element_by_id(Locators.password_passwordbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.login_button_id).click()

    def login_invalid(self):
        msg = self.driver.find_element_by_xpath(Locators.login_in_valid).text
        return msg