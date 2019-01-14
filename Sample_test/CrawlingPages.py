"""
พารามิเตอร์แรกของเมธอดจะเป็น self เสมอ ใช้เป็นตัวแปรในการอ้างถึงออบเจ็คปัจจุบัน
ในการเข้าถึงสมาชิกภายในออบเจ็คจะใช้เครื่องหมายจุด (.) ดังนั้นเมื่อเราเรียก b1.getDetail() จะเป็นการแสดงรายละเอียดข้อมูลในออบเจ็ค b1 ซึ่ง b2 ก็เช่นเดียวกัน
check package python = pip freeze | pip list
pip show html-testRunner
install Module PyCharm -> click Terminal -> pip install html-testRunner
"""
from selenium import webdriver
import unittest
import time
import HtmlTestRunner

class Craw_page(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test1(self):
        self.driver.get("https://www.apple.com/")
        ul = self.driver.find_elements_by_css_selector("[class^=ac-gn-header]")
        a = self.driver.find_elements_by_css_selector("[class^=ac-gn-link]")
        num_page_items = len(a)
        for i in range(num_page_items):
            click_link = a[i].get_attribute('href')
            print(click_link.click())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()