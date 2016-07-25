# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(c_firstname="denis2", c_middlename="2", c_lastname="nuzhdin", c_nickname="kashmir"))
    app.session.logout()
