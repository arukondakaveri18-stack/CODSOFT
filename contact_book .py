# CONTACT BOOK APPLICATION (PRELOADED DATA)

contacts = [
    {
        "name": "Arjun Reddy",
        "phone": "9876543210",
        "email": "arjun@gmail.com",
        "address": "Hyderabad"
    },
    {
        "name": "Priya Sharma",
        "phone": "9123456780",
        "email": "priya@gmail.com",
        "address": "Vijayawada"
    },
    {
        "name": "Rahul Kumar",
        "phone": "9988776655",
        "email": "rahul@gmail.com",
        "address": "Chennai"
    }
]

def show_menu():
    print("\n==============================")
    print("      CONTACT BOOK APP")
    print("==============================")
    print("1. View Contacts")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def view_contacts():
    print("\nContact List:")
    for i, c in enumerate(contacts):
        print(f"{i+1}. {c['name']} - {c['phone']}")

def search_contact():
    query = input("Enter name or phone to search: ")

    found = False
    for c in contacts:
        if query.lower() in c["name"].lower() or query in c["phone"]:
            print("\nContact Found:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True

    if not found:
        print("No contact found!")

def update_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to update: ")) - 1

        if 0 <= index < len(contacts):
            contacts[index]["name"] = "Updated Name"
            contacts[index]["phone"] = "0000000000"
            contacts[index]["email"] = "updated@gmail.com"
            contacts[index]["address"] = "Updated City"

            print("Contact updated successfully (auto values applied)!")
        else:
            print("Invalid selection!")

    except:
        print("Please enter a valid number!")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: ")) - 1

        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Deleted contact: {removed['name']}")
        else:
            print("Invalid selection!")

    except:
        print("Please enter a valid number!")

# MAIN LOOP
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        view_contacts()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")