class ContactHelper:

    def __init__(self, app):
        self.app = app

    def returne_home_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='nav']/ul/li[1]/a").click()

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.c_firstname)
        self.type("middlename", contact.c_middlename)
        self.type("lastname", contact.c_lastname)
        self.type("nickname", contact.c_nickname)
        self.type("title", contact.c_title)
        self.type("company", contact.c_company)
        self.type("address", contact.c_address)
        self.type("home", contact.c_home)
        self.type("mobile", contact.c_mobile)
        self.type("work", contact.c_work)
        self.type("fax", contact.c_fax)
        self.type("email", contact.c_email)
        self.type("email2", contact.c_email2)
        self.type("email3", contact.c_email3)
        self.type("homepage", contact.c_homepage)
        self.type("byear", contact.c_byear)
        self.type("ayear", contact.c_ayear)
        self.type("address2", contact.c_address2)
        self.type("phone2", contact.c_phone2)
        self.type("notes", contact.c_notes)

        # # Birthday
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[7]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[7]").click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").click()
        # # Anniversary
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[14]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[14]").click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").click()
        # # Group
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[2]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[2]").click()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def create(self, contact):
        wd = self.app.wd
        # open add form contact
        wd.find_element_by_link_text("add new").click()
        # fill contact
        self.fill_contact(contact)
        # submit contact
        wd.find_element_by_name("submit").click()
        self.returne_home_page()

    def edit_first_contact(self,new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # open edit form
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact
        self.fill_contact(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()
        # return home page
        self.returne_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # delete group
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # close alert
        wd.switch_to_alert().accept()


