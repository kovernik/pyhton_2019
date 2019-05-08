from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contact_list(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("Delete")) > 0):
            wd.find_element_by_link_text("home").click()

    def submit_delete_contact(self):
        wd = self.app.wd
        wd.switch_to_alert().accept()

    def create(self, contact):
        wd = self.app.wd
        self.new_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_list()
        # open modification form
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_list()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        self.submit_delete_contact()

    def count(self):
        wd = self.app.wd
        self.open_contact_list()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_list()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            cells = element.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_name("selected[]").get_attribute("value")
            lastname = cells[1].text
            firstname = cells[2].text
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts
