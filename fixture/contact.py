class ContactHelper:

    def __init__(self, app):
        self.app = app

    def returne_home_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='nav']/ul/li[1]/a").click()

    def fill_contact(self, contact):
        wd = self.app.wd
        # fill contact field
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.c_firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.c_middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.c_lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.c_nickname)

    def create(self, contact):
        wd = self.app.wd
        # open add form contact
        wd.find_element_by_link_text("add new").click()
        # fill contact
        self.fill_contact(contact)
        # submit contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit_first_contact(self,contact):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # open edit form
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact
        self.fill_contact(contact)
        # return home page
        self.returne_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # delete group
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # close alert
        wd.switch_to_alert().accept()


