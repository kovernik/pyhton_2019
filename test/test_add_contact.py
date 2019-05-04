from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Mikhail", lastname="Ko", nickname="motekito"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", nickname=""))
    app.session.logout()

