# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group (gr_name="testttt1", gr_header="tt1", gr_footer="tt2"))
