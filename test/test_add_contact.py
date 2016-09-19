# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="denis2",
                      lastname="nuzhdin",
                      notes="notes test"
                      # middlename="2",
                      # nickname="kashmir",
                      # title="home",
                      # company="myy company",
                      # address="my address",
                      # home="234", mobile="123-942-34-32",
                      # work="my work",
                      # fax="55-33-24",
                      # email="denis.nuzhdin@gmail.com",
                      # email2="---",
                      # email3="---",
                      # homepage="google.com",
                      # byear="1924",
                      # ayear="2311",
                      # address2="russia",
                      # phone2="439304393"
                      )
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1  == len(new_contacts)
    old_contacts.append (contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)


# def test_add_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group (gr_name="testttt1", gr_header="tt1", gr_footer="tt2")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len (old_groups) + 1 == len(new_groups)
#     old_groups.append (group)
#     assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)