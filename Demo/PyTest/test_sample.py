from selenium import webdriver
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Python_01/drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")


    def test_search(self,test_setup):
        driver.get("https://profile.hellosayhi.com/blog/")
        driver.find_element_by_id("s").send_keys("blog")
        driver.find_element_by_class_name("submit").click()
        x = driver.title
        assert x == "blog"

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")