# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Hagedoo(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_hagedoo(self):
        wd = self.wd
        wd.get("https://staging.hagedoo.de/")
        wd.find_element_by_xpath("submit-all-button()").click()
        # cookiebanner .submit-all-button
        wd.find_element_by_xpath("(//a[contains(text(),'Login')])[2]").click()
        wd.find_element_by_id("email-field").click()
        wd.find_element_by_id("email-field").clear()
        wd.find_element_by_id("email-field").send_keys("newuserworkspacekhb423@maildrop.cc")
        wd.find_element_by_id("password-field").click()
        wd.find_element_by_id("password-field").clear()
        wd.find_element_by_id("password-field").send_keys("123123")
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.find_element_by_xpath("//div[@id='__next']/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[7]/button/span").click()
        wd.find_element_by_xpath("//div[@id='__next']/div/div[2]/div/div/div/div/div[2]/a[3]/span").click()
        wd.find_element_by_xpath("//div[@id='__next']/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/p").click()
        wd.find_element_by_xpath("//div[@id='__next']/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/ul/li/div").click()
        wd.find_element_by_xpath("//div[@id='__next']/div/div[2]/div/div/div/div[4]/div/div/div/div[2]/div/ul/li[3]/a/span").click()
    
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
