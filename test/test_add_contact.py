# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(c_firstname="denis2", c_middlename="2", c_lastname="nuzhdin", c_nickname="kashmir", c_title="home", c_company="myy company", c_address="my address", c_home="234", c_mobile="123-942-34-32", c_work="my work", c_fax="55-33-24", c_email="denis.nuzhdin@gmail.com", c_email2="---", c_email3="---", c_homepage="google.com", c_byear="1924", c_ayear="2311", c_address2="russia", c_phone2="439304393", c_notes="notes test"))
