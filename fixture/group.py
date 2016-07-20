class GroupHelper:

    def __init__(self, app):
        self.app = app

    def returne_group_page(self):
        # return group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def create(self, group):
        # fill group
        wd = self.app.wd
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
        wd.find_element_by_name("submit").click()
        self.returne_group_page()