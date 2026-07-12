# Console-Based Contact Book (CLI)

A simple, interactive, and secure Command Line Interface (CLI) Contact Book application built using Python. This project demonstrates core programming concepts such as loops, conditional statements, nested dictionaries, and robust user input validation.

## Features

- **Add Contact:** Save a new contact with their Name, Phone Number, and Email.
- **Input Validation:** 
  - Prevents empty or blank names.
  - Ensures the phone number contains *only digits*.
  - Validates email addresses by checking for the `@` symbol.
  - Automatically cleans up extra trailing/leading spaces.
- **View All Contacts:** Lists all saved contacts in a clean, readable format.
- **Search Contact:** Instantly look up a contact's details by their name.
- **Delete Contact:** Remove an existing contact from the database securely.
- **Duplicate Prevention:** Alerts the user if they try to add a name that already exists.

## Concepts Demonstrated

- **Data Structures:** Nested Dictionaries (`contacts[name] = {"phone": ..., "email": ...}`)
- **Loops & Control Flow:** `while True`, nested input validation loops, and dictionary item unpacking (`.items()`).
- **String Methods:** `.strip()` for data cleaning and `.isdigit()` for type validation.

## How to Run

1. Make sure you have **Python 3** installed on your system.
2. Clone this repository or download the code file.
3. Open your terminal or command prompt, navigate to the project folder, and run:

```bash
python contact_book.py