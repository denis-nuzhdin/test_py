from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper (self)

    def returne_group_page(self):
        # return group page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def submit(self):
        # submit
        wd = self.wd
        wd.find_element_by_name("submit").click()
        self.returne_group_page()

    def fill_group(self, group):
        # fill group
        wd = self.wd
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

    def open_site(self):
        # open site
        wd = self.wd
        wd.get("http://macbook-pro-denis.local/addressbook/index.php")

    def destroy (self):
        self.wd.quit()