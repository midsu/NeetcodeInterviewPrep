class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def edit_contact(self, index, name, phone_number, email):
        contact = self.contacts[index]
        contact.name = name
        contact.phone_number = phone_number
        contact.email = email

    def delete_contact(self, index):
        del self.contacts[index]

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def show_all_contacts(self):
        for index, contact in enumerate(self.contacts):
            print(f"{index + 1}. {contact.name} - {contact.phone_number} - {contact.email}")

contact_list = ContactList()

while True:
    print("1. Add contact")
    print("2. Edit contact")
    print("3. Delete contact")
    print("4. Search contact")
    print("5. Show all contacts")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        contact = Contact(name, phone_number, email)
        contact_list.add_contact(contact)
        print("Contact added")

    elif choice == 2:
        index = int(input("Enter index of contact to edit: "))
        name = input("Enter new name: ")
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contact_list.edit_contact(index, name, phone_number, email)
        print("Contact edited")

    elif choice == 3:
        index = int(input("Enter index of contact to delete: "))
        contact_list.delete_contact(index)
        print("Contact deleted")

    elif choice == 4:
        name = input("Enter name to search: ")
        contact = contact_list.search_contact(name)
        if contact:
            print(f"{contact.name} - {contact.phone_number} - {contact.email}")
        else:
            print("Contact not found")

    elif choice == 5:
        contact_list.show_all_contacts()

    elif choice == 6:
        break

    else:
        print("Invalid choice")
