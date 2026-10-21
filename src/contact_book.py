"""Contact Book: stores contacts in a dictionary.

Each contact is stored as: name (lowercase) -> {"name", "phone", "email"}.
"""


def is_valid_phone(phone):
    """Check that a phone number has 7 to 15 digits.

    Spaces and dashes are ignored, and a leading + is allowed.

    Args:
        phone (str): The phone number to check.

    Returns:
        bool: True if the number looks valid.
    """
    digits = phone.replace(" ", "").replace("-", "").lstrip("+")
    return digits.isdigit() and 7 <= len(digits) <= 15


def is_valid_email(email):
    """Check that an email is empty or has an @ followed by a dot.

    Args:
        email (str): The email address to check.

    Returns:
        bool: True if the email is empty or looks valid.
    """
    if not email:
        return True
    return "@" in email and "." in email.split("@")[-1]


def add_contact(contacts, name, phone, email=""):
    """Add a new contact.

    Args:
        contacts (dict): The contact book.
        name (str): The contact's name.
        phone (str): The contact's phone number.
        email (str): The contact's email (optional).

    Returns:
        bool: True if added, False if that name already exists.
    """
    key = name.strip().lower()
    if key in contacts:
        return False
    contacts[key] = {"name": name.strip(), "phone": phone, "email": email}
    return True


def update_contact(contacts, name, phone=None, email=None):
    """Update the phone and/or email of an existing contact.

    Args:
        contacts (dict): The contact book.
        name (str): The name of the contact to update.
        phone (str or None): New phone, or None to keep the old one.
        email (str or None): New email, or None to keep the old one.

    Returns:
        bool: True if updated, False if the contact does not exist.
    """
    key = name.strip().lower()
    if key not in contacts:
        return False
    if phone is not None:
        contacts[key]["phone"] = phone
    if email is not None:
        contacts[key]["email"] = email
    return True


def delete_contact(contacts, name):
    """Delete a contact.

    Args:
        contacts (dict): The contact book.
        name (str): The name of the contact to delete.

    Returns:
        bool: True if deleted, False if the contact does not exist.
    """
    key = name.strip().lower()
    if key not in contacts:
        return False
    del contacts[key]
    return True


def search_contacts(contacts, keyword):
    """Find contacts whose name contains a keyword (ignoring case).

    Args:
        contacts (dict): The contact book.
        keyword (str): The text to look for.

    Returns:
        dict: The matching contacts. Empty if there are none.
    """
    keyword = keyword.strip().lower()
    if not keyword:
        return {}
    return {key: value for key, value in contacts.items() if keyword in key}


def format_contacts(contacts):
    """Return contacts as text, sorted by name.

    Args:
        contacts (dict): The contacts to format.

    Returns:
        str: One contact per line, or a message if there are none.
    """
    if not contacts:
        return "No contacts found."
    lines = []
    for key in sorted(contacts):
        contact = contacts[key]
        email = contact["email"] or "no email"
        lines.append(f"{contact['name']} | {contact['phone']} | {email}")
    return "\n".join(lines)


def ask_text(prompt):
    """Ask for text until the user types something non-empty."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field cannot be empty.")


def ask_phone(prompt):
    """Ask for a phone number until a valid one is entered."""
    while True:
        phone = input(prompt).strip()
        if is_valid_phone(phone):
            return phone
        print("Enter 7 to 15 digits (spaces, dashes and + are allowed).")


def ask_email(prompt):
    """Ask for an email until a valid one, or nothing, is entered."""
    while True:
        email = input(prompt).strip()
        if is_valid_email(email):
            return email
        print("Enter a valid email like name@example.com, or leave blank.")


MENU = """
===== Contact Book =====
1. Add contact
2. View all contacts
3. Search contacts
4. Update contact
5. Delete contact
6. Exit
"""


def handle_add(contacts):
    """Ask for details and add a contact."""
    name = ask_text("Name: ")
    phone = ask_phone("Phone: ")
    email = ask_email("Email (optional): ")
    if add_contact(contacts, name, phone, email):
        print(f"Added {name}.")
    else:
        print(f"{name} already exists. Use Update to change it.")


def handle_update(contacts):
    """Ask who to update and what to change."""
    name = ask_text("Name of the contact to update: ")
    if name.lower() not in contacts:
        print(f"No contact named {name}.")
        return
    print("Leave a field blank to keep the current value.")
    phone = input("New phone: ").strip()
    while phone and not is_valid_phone(phone):
        phone = input("Invalid phone. Try again or leave blank: ").strip()
    email = input("New email: ").strip()
    while email and not is_valid_email(email):
        email = input("Invalid email. Try again or leave blank: ").strip()
    update_contact(contacts, name, phone or None, email or None)
    print(f"Updated {name}.")


def main():
    """Run the contact book menu until the user exits."""
    contacts = {}
    while True:
        print(MENU)
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            handle_add(contacts)
        elif choice == "2":
            print(format_contacts(contacts))
        elif choice == "3":
            keyword = input("Search for: ")
            print(format_contacts(search_contacts(contacts, keyword)))
        elif choice == "4":
            handle_update(contacts)
        elif choice == "5":
            name = ask_text("Name of the contact to delete: ")
            if delete_contact(contacts, name):
                print(f"Deleted {name}.")
            else:
                print(f"No contact named {name}.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()