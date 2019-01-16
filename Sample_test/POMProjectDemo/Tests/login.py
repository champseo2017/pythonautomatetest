from selenium import webdriver
import time
import unittest
from Sample_test.POMProjectDemo.Pages.loginPage import LoginPage #import POM login page webelement + method
from Sample_test.POMProjectDemo.Pages.homePage import HomePage #import POM login page webelem

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/pythonautomatetest/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_login_valid(self):
        driver = self.driver
        driver.get("http://webblog.hellosayhi.com/login")

        login = LoginPage(driver)
        login.enter_email("user01@user01.com")
        login.enter_password("123456")
        login.click_login()

        homepage = HomePage(driver)
        homepage.print_welcome_login()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()
