# Contact Book Program

contacts = []

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter 10-digit phone number: ").strip()

    if not is_valid_phone(phone):
        print(" Invalid phone number. Must be 10 digits and numeric.")
        return

    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    print(f" Contact '{name}' added successfully!")

def display_contacts():
    if not contacts:
        print(" Contact book is empty.")
        return

    print("\n All Contacts:")
    print("-" * 30)
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")
    print("-" * 30)

def search_contact():
    query = input("Enter name to search: ").strip().lower()
    found = False

    print("\n Search Results:")
    for contact in contacts:
        if contact["name"].lower() == query:
            print(f" Name: {contact['name']}, Phone: {contact['phone']}")
            found = True

    if not found:
        print(f" No contact found with name '{query}'.")

def contact_book_menu():
    while True:
        print("\n======= Contact Book Menu =======")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    contact_book_menu()
