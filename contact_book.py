# contact information    name,phone number,email,address
# add contact            new contact with their details
# view contact list      display all saved contact with names and phone numbers 
# search contact         search fun to find contacts by name or phone number
# update contact 
# delete contact



# Creating empty dictionary to store contacts details 
contact_book = {}                           

# function to add contacts 
def add_contact (name,phone,email,address):
    contact_book[name] = {
        "phone" : phone,
        "email" : email,
        "address" : address
    }
    print ("Contact Details of",name,"added successfully!")

# function to view all contacts 
def view_contact():
    if not contact_book:
        print("No contacts found")
    else:
        print("Contact list is :- ")
        for name,details in contact_book.items():           #using items() function where key:value pair is stored in the form of tuple.
            print(name,":",details["phone"])


# function to search contact
def search_contact(name):
    # name1 = name.lower()
    if name not in contact_book:
        print("Contact not found")
    else:
        details = contact_book[name]
        print("Contact Found:")
        print("Name:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])
        print("Address:", details["address"])
        

# function to update contact details
def update_contact(name, phone=None, email=None, address=None):
    if name in contact_book:
        if phone: contact_book[name]["phone"] = phone
        if email: contact_book[name]["email"] = email
        if address: contact_book[name]["address"] = address
        print("Contact",name,"updated successfully!")
    else:
        print("Contact not found.")
    
# function to delete contact
def del_contact(name):
    if name in contact_book:
        del contact_book[name]
        print("Contact",name,"deleted successfully")
    else:
        print("Contact not found")



# main function
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add contact")
    print("2. View contact list")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(name, phone, email, address)

    elif ch == "2":
        view_contact()
    
    elif ch == "3":
        name = input("Enter name to be searched: ")
        search_contact(name)

    elif ch == "4":
        name = input("Enter name to update details: ")
        phone = input("Enter new Phone (leave blank if no change): ")
        email = input("Enter new Email (leave blank if no change): ")
        address = input("Enter new Address (leave blank if no change): ")
        update_contact(name, phone if phone else None,
                             email if email else None,
                             address if address else None)
    
    elif ch == "5":
        name = input("Enter name of contact to be deleted: ")
        del_contact(name)

    elif ch == "6":
        print("Contact Book Exited.")
        break

    else:
        print("Invalid choice.Enter between(1-5)")
    


