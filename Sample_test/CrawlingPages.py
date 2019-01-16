from selenium import webdriver
import unittest
import HtmlTestRunner
import time

class CrawlingPages(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://www.apple.com/")
        ul = self.driver.find_elements_by_css_selector("[class^=ac-gn-header]")
        a = self.driver.find_elements_by_css_selector("[class^=ac-gn-link]")
        num_page_items = len(a)
        for i in range(num_page_items):
            click_link = a[i].get_attribute('href')
            print(click_link)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()
