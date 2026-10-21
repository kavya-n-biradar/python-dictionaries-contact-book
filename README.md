# Python Dictionaries: Data Organization and Contact Book

A beginner Python project for the CodeMore Python Programming Internship (Week 3, Task 1). It uses dictionaries to store and manage structured data, with a Contact Book as the mini task.

## Project Overview

- `src/dictionary_basics.py` shows how to create, access, update, delete and iterate over dictionaries, including nested dictionaries.
- `src/contact_book.py` is a menu-driven Contact Book. Contacts are stored in a dictionary, and you can add, view, search, update and delete them.

## Project Structure

```
python-dictionaries-contact-book/
├── README.md
├── .gitignore
├── src/
│   ├── dictionary_basics.py
│   └── contact_book.py
└── docs/
    └── screenshots/
```

## Requirements

- Python 3.8 or newer. No external libraries.

## Setup and How to Run

```bash
git clone https://github.com/kavya-n-biradar/python-dictionaries-contact-book.git
cd python-dictionaries-contact-book
python src/dictionary_basics.py
python src/contact_book.py
```

## How the Contact Book Uses Dictionaries

Each contact is stored as a dictionary inside another dictionary:

```python
contacts = {
    "asha rao": {"name": "Asha Rao", "phone": "98765 43210", "email": "asha@example.com"},
}
```

The lowercase name is the key, so lookups ignore upper and lower case. The value is another dictionary holding the contact's details.

| Feature | Dictionary operation used |
|---|---|
| Add | `contacts[key] = {...}` after checking `key in contacts` |
| Update | `contacts[key]["phone"] = new_phone` |
| Delete | `del contacts[key]` |
| Search | A dictionary comprehension that keeps keys containing the keyword |
| View | `sorted(contacts)` and a loop over the keys |

Edge cases handled: empty contact book, duplicate names, empty fields, invalid phone numbers and emails, contacts that don't exist, and invalid menu choices.

## Dictionary Concepts Learned

- A dictionary stores **key-value pairs**, and keys must be unique.
- `d[key]` reads a value, and `d.get(key, default)` reads it safely.
- `d[key] = value` adds a new key or updates an existing one.
- `pop()` and `del` remove keys.
- `in` checks whether a key exists.
- `.keys()`, `.values()` and `.items()` let you loop through a dictionary.
- Dictionaries can be nested to organise structured data.

## Console Output

### `dictionary_basics.py` (shortened)
```
3. After updating marks and adding grade:
{'name': 'Kavya', 'age': 22, 'course': 'Python', 'marks': 91.0, 'grade': 'A'}

7. Nested dictionary:
S1: Asha scored 82
S2: Ravi scored 67
S3: Meera scored 91
Average marks: 80.0
```

### `contact_book.py` (shortened)
```
Added Asha Rao.
Added Ravi Kumar.
Asha Rao | 98765 43210 | asha@example.com
Ravi Kumar | +91-9123456780 | no email
Deleted Ravi Kumar.
```
### Screenshots

Full screenshots are in [`docs/screenshots/`](docs/screenshots/):
- `dictionary_basics_part1.png` and `dictionary_basics_part2.png`: output of `dictionary_basics.py`
- `contact_book_full_session1.png` and `contact_book_full_session2.png`: a full Contact Book session (add, view, search, update, delete and invalid input)

## What I Learned

- How dictionaries store related data and why they are useful for records
- How to add, update, delete and loop through dictionary data
- How to nest dictionaries and use dictionary comprehensions
- How to validate user input in a menu-driven program

## Author

Kavya Biradar