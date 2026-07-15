# Contact Book CLI
import json
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}

print("\nConsole based Contact Book")

while True:
    print("\n1.Add Contact \n2.View All Contacts \n3.Search Contact \n4.Delete Contact \n5.Exit")
    choice = input("Select an option: ")
    print() 
    
    if choice == "1":
        name = input("Enter Name: ")
        while name.strip() == "" or not name.replace(" ", "").isalpha():
            print("Name can only contain letters and spaces!")
            name = input("Enter Name: ")
            
        if name in contacts:
            print(f"\n{name} already exists. Choose different name..!")
        else:
            phone = input("Enter phone number: ")
            
            while not phone.isdigit():
                print("Only digits are allowed..!")
                phone = input("Enter phone number: ")
                
            email = input("Enter email: ")
            
            while '@' not in email:
                print("Invalid email..!")
                email = input("Enter email: ")
            
            name = name.strip()
            contacts[name] = {"phone": phone, "email": email}
            print(f"\n{name} added successfully..!")
            with open("contacts.json", "w") as file:
                json.dump(contacts, file, indent=4)
            
    elif choice == "2":
        print("Viewing all contacts:\n")
        if not contacts:
            print("No contacts found..!")
        for key, value in contacts.items():
            print(f"{key} - Phone: {value['phone']} - Email: {value['email']}")
    
    elif choice == "3":
        search_name = input("Enter name to search: ")
        print()
        if search_name in contacts:
            print(f"{search_name} - Phone: {contacts[search_name]['phone']} - Email: {contacts[search_name]['email']}")
        else:
            print(f"{search_name} not in contacts")
            
    elif choice == "4":
        del_contact = input("Enter contact to delete: ")
        if del_contact in contacts:
            del contacts[del_contact]
            print(f"\n{del_contact} deleted successfully..!")
            with open("contacts.json", "w") as file:
                json.dump(contacts, file, indent=4)
        else:
            print(f"\n{del_contact} not found.. !")
    
    elif choice == "5":
        print("Thank you for using the System..!!\n")
        break
    else:
        print("Invalid choice..! Try Again")
