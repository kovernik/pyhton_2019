from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Mikhail", lastname="Ko", nickname="motekito"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", nickname=""))

