# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from  group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.fill_group(wd, Group (gr_name="test1", gr_header="tt1", gr_footer="tt2"))
        self.submit(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def returne_group_page(self, wd):
        # return group page
        wd.find_element_by_link_text("group page").click()

    def submit(self, wd):
        # submit
        wd.find_element_by_name("submit").click()
        self.returne_group_page(wd)

    def fill_group(self, wd, group):
        # fill group
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.gr_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.gr_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.gr_footer)

    def login(self, wd, username, password):
        # login
        self.open_site(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_site(self, wd):
        # open site
        wd.get("http://macbook-pro-denis.local/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
