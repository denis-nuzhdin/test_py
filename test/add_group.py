# -*- coding: utf-8 -*-
import pytest
from  fixture.application import Application
from  model.group import Group


@pytest.fixture()
def app(request):
    fixture = Application ()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.fill_group(Group (gr_name="test1", gr_header="tt1", gr_footer="tt2"))
    app.submit()
    app.session.logout()