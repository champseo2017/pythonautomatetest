from Sample_test.POMProjectDemo.Locators.locators import Locators #import locators
class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.welcome_session = Locators.welcome_session


    def print_welcome_login(self):
        element_success = self.driver.find_element_by_css_selector(Locators.welcome_session)
        print(element_success.text)

