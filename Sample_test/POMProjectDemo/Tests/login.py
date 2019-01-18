from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Sample_test.POMProjectDemo.Pages.loginPage import LoginPage #import POM login page webelement + method
from Sample_test.POMProjectDemo.Pages.homePage import HomePage #import POM login page webelem
import HtmlTestRunner

# Run cd C:\pythonautomatetest -> python -m Sample_test.POMProjectDemo.Tests.login
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/pythonautomatetest/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_02_login_valid(self):
        driver = self.driver
        driver.get("http://webblog.hellosayhi.com/login")

        login = LoginPage(driver)
        login.enter_email("user01@user01.com")
        login.enter_password("123456")
        login.click_login()

        homepage = HomePage(driver)
        homepage.print_welcome_login()
        time.sleep(5)

    def test_01_login_invalid(self):
        driver = self.driver
        driver.get("http://webblog.hellosayhi.com/login")

        login = LoginPage(driver)
        login.enter_email("user01123@user01.com")
        login.enter_password("123456")
        login.click_login()

        message = login.login_invalid()
        # print(message) # return login page
        self.assertEqual(message, "Error Invalid email.")

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/pythonautomatetest/reports'))
    # unittest.main()
