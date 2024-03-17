# Import necessary modules
import os

# Define the contact class
class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

# Define the contact manager class
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print(f"{contact.name} - {contact.phone_number}")

    def search_contact(self, name_or_phone_number):
        for contact in self.contacts:
            if contact.name == name_or_phone_number or contact.phone_number == name_or_phone_number:
                return contact
        return None

    def update_contact(self, contact, new_name, new_phone_number, new_email, new_address):
        contact.name = new_name
        contact.phone_number = new_phone_number
        contact.email = new_email
        contact.address = new_address

    def delete_contact(self, contact):
        self.contacts.remove(contact)

# Create a contact manager object
contact_manager = ContactManager()

# Add some contacts
contact_manager.add_contact(Contact("John Doe", "0123456789", "john.doe@example.com", "123 Main Street"))
contact_manager.add_contact(Contact("Jane Doe", "9876543210", "jane.doe@example.com", "456 Elm Street"))

# View the contact list
contact_manager.view_contact_list()

# Search for a contact
contact = contact_manager.search_contact("John Doe")
if contact is not None:
    print(f"Found contact: {contact.name}")
else:
    print("Contact not found")

# Update a contact
contact_manager.update_contact(contact, "John Smith", "0987654321", "john.smith@example.com", "789 Oak Street")

# Delete a contact
contact_manager.delete_contact(contact)

# View the contact list again
contact_manager.view_contact_list()
