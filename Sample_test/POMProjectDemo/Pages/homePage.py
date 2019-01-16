class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.welcome_session = "div.alert-success"

    def print_welcome_login(self):
        element_success = self.driver.find_element_by_css_selector(self.welcome_session)
        print(element_success.text)