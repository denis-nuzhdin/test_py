from model.group import Group


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(gr_name="edit_test111111"))
