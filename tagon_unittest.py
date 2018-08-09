import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class testClass(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        baseURL = "http://tagonsupport.cubixsource.com/administrator/login"
        cls.driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get(baseURL)

    def test_class(self):
        a = self.driver.find_element(By.NAME, "email")
        self.assertTrue(a, "'a' is not True")
        a.send_keys("admin@tagonapp.com")

    def test_class2(self):
        b = self.driver.find_element(By.NAME, "password")
        self.assertTrue(b, "'b' is not True")
        b.send_keys("admin123")

    def test_class3(self):
        c = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        self.assertTrue(c, "'c' is not True")
        c.click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("case ended")


if __name__ == '__main__':
    unittest.main(verbosity=2)
