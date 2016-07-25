from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(gr_name="edit_test1", gr_header="e_tt1", gr_footer="e_tt2"))
    app.session.logout()
