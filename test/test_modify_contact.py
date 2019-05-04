from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname="Mikhail1", lastname="Ko1", nickname="motekito1"))
    app.session.logout()
