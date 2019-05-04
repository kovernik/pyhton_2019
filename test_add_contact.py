from contact import Contact
from application_contact import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_contact_page()
    app.create_contact(Contact(firstname="Mikhail", lastname="Ko", nickname="motekito"))
    app.logout()


def test_add_empty_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_contact_page()
    app.create_contact(Contact(firstname="", lastname="", nickname=""))
    app.logout()

