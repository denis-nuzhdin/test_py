from model.contact import Contact

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
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        self.type("notes", contact.notes)
        # self.type("middlename", contact.middlename)
        # self.type("nickname", contact.nickname)
        # self.type("title", contact.title)
        # self.type("company", contact.company)
        # self.type("address", contact.address)
        # self.type("home", contact.home)
        # self.type("mobile", contact.mobile)
        # self.type("work", contact.work)
        # self.type("fax", contact.fax)
        # self.type("email", contact.email)
        # self.type("email2", contact.email2)
        # self.type("email3", contact.email3)
        # self.type("homepage", contact.homepage)
        # self.type("byear", contact.byear)
        # self.type("ayear", contact.ayear)
        # self.type("address2", contact.address2)
        # self.type("phone2", contact.phone2)


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

    def count(self):
        wd = self.app.wd
        self.returne_home_page()
        return len(wd.find_elements_by_name("selected[]"))

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
        self.returne_home_page()
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
        # self.returne_home_page()
        self.select_first_contact()
        # delete group
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # close alert
        wd.switch_to_alert().accept()

    def get_contact_list(self):
        wd = self.app.wd
        self.returne_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            firstname = element.find_element_by_css_selector("td:nth-child(3)").text
            # lastname = element.find_elements_by_css_selector("td:nth-child(2)")
            contacts.append(Contact(id=id, firstname=firstname))
        return contacts

    # def get_group_list(self):
    #     wd = self.app.wd
    #     self.open_group_page()
    #     groups = []
    #     for element in wd.find_elements_by_css_selector("span.group"):
    #         text = element.text
    #         id = element.find_element_by_name("selected[]").get_attribute("value")
    #         groups.append(Group(gr_name=text,id=id))
    #     return groups