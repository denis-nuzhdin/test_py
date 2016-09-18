from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="for edit username", middlename="for edit middlename",))

    app.contact.edit_first_contact(Contact(firstname="__edit_firstname__", middlename="__edit_middlename__", lastname="__edit_lastname__", nickname="__edit_nickname__"))