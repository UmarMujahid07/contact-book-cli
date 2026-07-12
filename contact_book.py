# Contact Book CLI
contacts = {}
print("Console based Contact Book")

while True:
    print("1.Add Contact \n2.View All Contacts \n3.Search Contact \n4.Delete Contact \n5.Exit")
    choice= input("Slect an option: ")
    
    if choice== "1":
        name= input("Enter Name: ")
        while name.strip() == "":
            print("Name can not be empty..!")
            name= input("Enter Name: ")
            
        if name in contacts:
            print(f"{name} already exists. Choose different name..!")
        else:
            phone = input("Enter phone number: ")
            
            while not phone.isdigit():
                print("Only digits are allowed..!")
                phone=input("Enter phone number: ")
                
            email = input("Enter email: ")
            
            while '@' not in email:
                print("Invalid email..!")
                email = input("Enter email: ")
            
            name = name.strip()
            contacts[name] = {"phone": phone, "email": email}
            print(f"{name} added successfully..!")
            
    elif choice == "2":
        print("Viewing all contacts: ")
        if not contacts:
            print("No contacts found..!")
        for key, value in contacts.items():
            print(f"{key} - Phone: {value['phone']}, Email: {value['email']}")
    
    elif choice=="3":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"{search_name} - Phone: {contacts[search_name]['phone']}- Email: {contacts[search_name]['email']}")
        else:
            print(f"{search_name} not in contacts")
            
    elif choice == "4":
        del_contact = input("Enter contact to delete: ")
        if del_contact in contacts:
            del contacts[del_contact]
            print(f"{del_contact} deleted successfully..!")
        else:
            print(f"{del_contact} not found.. !")
            
    elif choice == "5":
        print("Thank you for using the System..!!")
        break
    else:
        print("Invalid choice..! Try Again")