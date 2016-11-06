# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="denis2",
                      lastname="nuzhdin",
                      notes="notes test",
                      home="1111",
                      mobile="123-942-34-32",
                      work="3333",
                      phone2="439304393"
                      # middlename="2",
                      # nickname="kashmir",
                      # title="home",
                      # company="myy company",
                      # address="my address",

                      # fax="55-33-24",
                      # email="denis.nuzhdin@gmail.com",
                      # email2="---",
                      # email3="---",
                      # homepage="google.com",
                      # byear="1924",
                      # ayear="2311",
                      # address2="russia",

                      )
    app.contact.create(contact)
    assert len(old_contacts) + 1  == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append (contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)


# def test_add_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group (gr_name="testttt1", gr_header="tt1", gr_footer="tt2")
#     app.group.create(group)
#     assert len (old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append (group)
#     assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)