from model.contact import Contact
from random import randrange


def test_contact_by_index(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="for edit username", lastname="for edit lastname",))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="__edit_firstname__",
                      lastname="__edit_lastname__",
                      home="555",
                      mobile="5555",
                      work="55555",
                      phone2="555555")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index]=contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

