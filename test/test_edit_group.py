from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() ==0:
        app.group.create(Group(gr_name="for edit group"))
    app.group.edit_first_group(Group(gr_name="edit_test111111"))
