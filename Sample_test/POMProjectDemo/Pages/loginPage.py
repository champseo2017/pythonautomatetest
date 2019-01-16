class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.email_emailbox_id = "email"
        self.password_passwordbox_id = "password"
        self.login_button_id = "//button[@type='submit']"

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_emailbox_id).clear()
        self.driver.find_element_by_id(self.email_emailbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_passwordbox_id).clear()
        self.driver.find_element_by_id(self.password_passwordbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_id).click()