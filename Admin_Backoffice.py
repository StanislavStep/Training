# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AdminBackoffice(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_admin_backoffice(self):
        wd = self.wd
        wd.get("https://backoffice.dev.gatech.name/login")
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("perf_a2")
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("UpWorkSuper")
        wd.find_element_by_xpath("//div[2]/button/span").click()
        wd.find_element_by_xpath("//div[@id='statusSelect']/div/div/div/div").click()
        wd.find_element_by_id("react-select-3-option-2").click()
        wd.find_element_by_xpath("//div[@id='methodSelect']/div/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='root']/div/div/div[3]/div/main/div").click()
        wd.find_element_by_xpath("//td[@id='id_0']/span/span").click()
        wd.find_element_by_xpath("//div[@id='root']/div/div/div[4]/div/div/div[6]/div/button/span").click()
        wd.find_element_by_css_selector("button.MuiButtonBase-root.MuiIconButton-root.jss915.jss916.MuiPaper-elevation9 > span.MuiIconButton-label > svg.MuiSvgIcon-root > path").click()
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
