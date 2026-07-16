# Contact Book CLI - OOP Refactored
import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name.strip()
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"phone": self.phone, "email": self.email}


class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, contact: Contact):
        if contact.name in self.contacts:
            print(f"\n{contact.name} already exists. Choose a different name..!")
            return False
        
        self.contacts[contact.name] = contact.to_dict()
        self._save_contacts()
        print(f"\n{contact.name} added successfully..!")
        return True

    def view_all_contacts(self):
        print("Viewing all contacts:\n")
        if not self.contacts:
            print("No contacts found..!")
            return
        for name, details in self.contacts.items():
            print(f"{name} - Phone: {details['phone']} - Email: {details['email']}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name} - Phone: {self.contacts[name]['phone']} - Email: {self.contacts[name]['email']}")
        else:
            print(f"{name} not in contacts")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self._save_contacts()
            print(f"\n{name} deleted successfully..!")
        else:
            print(f"\n{name} not found..!")


# main( )
def main():
    book = ContactBook()
    print("\nConsole based Contact Book")

    while True:
        print("\n1.Add Contact \n2.View All Contacts \n3.Search Contact \n4.Delete Contact \n5.Exit")
        choice = input("Select an option: ")
        print()  # Spacing

        if choice == "1":
            name = input("Enter Name: ")
            while name.strip() == "" or not name.replace(" ", "").isalpha():
                print("Name can only contain letters and spaces!")
                name = input("Enter Name: ")

            phone = input("Enter phone number: ")
            while not phone.isdigit():
                print("Only digits are allowed..!")
                phone = input("Enter phone number: ")

            email = input("Enter email: ")
            while '@' not in email:
                print("Invalid email..!")
                email = input("Enter email: ")

            # Creating Object and passing to Book
            new_contact = Contact(name, phone, email)
            book.add_contact(new_contact)

        elif choice == "2":
            book.view_all_contacts()

        elif choice == "3":
            search_name = input("Enter name to search: ")
            print()
            book.search_contact(search_name)

        elif choice == "4":
            del_contact = input("Enter contact to delete: ")
            book.delete_contact(del_contact)

        elif choice == "5":
            print("Thank you for using the System..!!\n")
            break
        else:
            print("Invalid choice..! Try Again")

if __name__ == "__main__":
    main()