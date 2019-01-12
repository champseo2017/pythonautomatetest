"""
พารามิเตอร์แรกของเมธอดจะเป็น self เสมอ ใช้เป็นตัวแปรในการอ้างถึงออบเจ็คปัจจุบัน
ในการเข้าถึงสมาชิกภายในออบเจ็คจะใช้เครื่องหมายจุด (.) ดังนั้นเมื่อเราเรียก b1.getDetail() จะเป็นการแสดงรายละเอียดข้อมูลในออบเจ็ค b1 ซึ่ง b2 ก็เช่นเดียวกัน
check package python = pip freeze | pip list
pip show html-testRunner
install Module PyCharm -> click Terminal -> pip install html-testRunner
"""
from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()

    def test_search_ggwp(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("ggwp")
        self.driver.find_element_by_name("btnK1").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Python_01/reports'))









