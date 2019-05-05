from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="New lastname"))
