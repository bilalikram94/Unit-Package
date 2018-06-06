import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class TagOnSmokeTest(unittest.TestCase):
    driver = None
    actions = None

    @classmethod
    def setUpClass(cls):
        baseURL = "http://tagonsupport.cubixsource.com/administrator/login"
        cls.driver = webdriver.Chrome("")
        cls.driver.maximize_window()
        cls.driver.get(baseURL)
        cls.actions = ActionChains(cls.driver)

    def test_class(self):
        a = self.driver.find_element(By.NAME, "email")
        self.assertTrue(a, "'a' is not True")
        a.send_keys("your@email.com")

    def test_class2(self):
        b = self.driver.find_element(By.NAME, "password")
        self.assertTrue(b, "'b' is not True")
        b.send_keys("your@password")

    def test_class3(self):
        c = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        self.assertTrue(c, "'c' is not True")
        c.click()
        time.sleep(3)

    def test_sidemenu(self):
        sideBtn = self.driver.find_element(By.LINK_TEXT, "Dashboard")
        self.assertTrue(sideBtn, "sideBtn is not True")
        time.sleep(3)

    def test_sidemenu1(self):
        sideBtn = self.driver.find_element(By.LINK_TEXT, "Admins Management")
        self.assertTrue(sideBtn, "sideBtn is not True")
        time.sleep(3)

    def test_sidemenu2(self):
        sideBtn = self.driver.find_element(By.LINK_TEXT, "CMS Pages")
        self.assertTrue(sideBtn, "sideBtn is not True")
        time.sleep(3)

    def test_menuaction(self):
        menuAction = self.driver.find_element(By.CSS_SELECTOR, ".menu-actions")
        self.assertTrue(menuAction, "menuAction is not True")
        time.sleep(3)

    def test_select(self):
        select = self.driver.find_element(By.CSS_SELECTOR, "select")
        self.assertTrue(select, "Select is not True")
        time.sleep(3)

    def test_zogout(self):
        time.sleep(3)
        hidden = self.driver.find_element(By.CSS_SELECTOR, ".logged-user-i")
        self.assertTrue(hidden, "Logout is not True")
        self.actions.move_to_element(hidden).perform()
        logout = self.driver.find_element(By.LINK_TEXT, "Logout")
        self.assertTrue(logout, "Logout is not true")
        self.actions.move_to_element(logout).click().perform()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
