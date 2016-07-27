from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count()==0:
        app.contact.create(Contact(c_firstname="for edit username", c_middlename="for edit middlename",))

    app.contact.edit_first_contact(Contact(c_firstname="__edit_firstname__", c_middlename="__edit_middlename__", c_lastname="__edit_lastname__", c_nickname="__edit_nickname__"))