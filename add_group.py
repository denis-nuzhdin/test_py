# -*- coding: utf-8 -*-
import pytest
from  group import Group
from  application import Application


@pytest.fixture()
def app(request):
    fixture = Application ()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.fill_group(Group (gr_name="test1", gr_header="tt1", gr_footer="tt2"))
    app.submit()
    app.logout()
