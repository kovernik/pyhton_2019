from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname for modify"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="lastname for modify"))
    app.contact.modify_first_contact(Contact(lastname="New lastname"))
