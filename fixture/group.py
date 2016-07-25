class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def returne_group_page(self):
        wd = self.app.wd
        # return group page
        wd.find_element_by_link_text("group page").click()

    def fill_group(self, group):
        wd = self.app.wd
        # fill group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.gr_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.gr_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.gr_footer)

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # open add form
        wd.find_element_by_name("new").click()
        # fill group
        self.fill_group(group)
        # submit group
        wd.find_element_by_name("submit").click()
        self.returne_group_page()

    def edit_first_group(self,group):
        wd = self.app.wd
        # open group page
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # open edit form
        wd.find_element_by_name("edit").click()
        # fill group
        self.fill_group(group)
        # update group
        wd.find_element_by_name("update").click()
        # returne group page
        self.returne_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        # open group page
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # delete group
        wd.find_element_by_name("delete").click()
        # returne group page
        self.returne_group_page()