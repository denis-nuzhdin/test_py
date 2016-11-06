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
        self.type("home", contact.home)
        self.type("mobile", contact.mobile)
        self.type("work", contact.work)
        self.type("phone2", contact.phone2)
        # self.type("middlename", contact.middlename)
        # self.type("nickname", contact.nickname)
        # self.type("title", contact.title)
        # self.type("company", contact.company)
        # self.type("address", contact.address)

        # self.type("fax", contact.fax)
        # self.type("email", contact.email)
        # self.type("email2", contact.email2)
        # self.type("email3", contact.email3)
        # self.type("homepage", contact.homepage)
        # self.type("byear", contact.byear)
        # self.type("ayear", contact.ayear)
        # self.type("address2", contact.address2)


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


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
        self.contact_cach = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.returne_home_page()
        self.select_contact_by_index(index)
        # open edit form
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact(new_contact_data)
        wd.find_element_by_name("update").click()
        self.returne_home_page()
        self.contact_cach = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.returne_home_page()
        self.select_contact_by_index(index)
        # delete group
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # close alert
        wd.switch_to_alert().accept()
        self.contact_cach = None

    contact_cach = None

    def get_contact_list(self):
        if self.contact_cach is None:
            wd = self.app.wd
            self.returne_home_page()
            self.contact_cach = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                self.contact_cach.append(Contact(id=id, firstname=firstname,lastname=lastname))
        return list(self.contact_cach)


