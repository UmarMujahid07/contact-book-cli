# Console-Based Contact Book (CLI) with JSON Storage 

A simple, interactive, and secure Command Line Interface (CLI) Contact Book application built using Python. This project demonstrates core programming concepts such as loops, conditional statements, nested dictionaries, robust user input validation, and permanent data storage.

## Features

- **JSON Data Persistence:** Automatically saves and loads your contact list to/from a local `contacts.json` file. Your data is never lost when you close the application!
- **Add Contact:** Save a new contact with their Name, Phone Number, and Email.
- **Input Validation:** 
  - Prevents empty or blank names using `.strip()`.
  - Ensures the phone number contains *only digits* using `.isdigit()`.
  - Validates email addresses by checking for the `@` symbol.
- **View All Contacts:** Lists all saved contacts in a clean, readable format.
- **Search Contact:** Instantly look up a contact's details by their name.
- **Delete Contact:** Remove an existing contact from the database securely (and updates the JSON file automatically).
- **Duplicate Prevention:** Alerts the user if they try to add a name that already exists.

## Concepts Demonstrated

- **File Handling & Serialization:** Utilizing Python's native `json` module (`json.dump()` and `json.load()`) to serialize nested Python dictionaries into readable JSON files.
- **Exception Handling:** Using `try-except` blocks to handle `FileNotFoundError` gracefully when reading the database for the first time.
- **Data Structures:** Nested Dictionaries (`contacts[name] = {"phone": ..., "email": ...}`)
- **Loops & Control Flow:** `while True`, nested input validation loops, and dictionary item unpacking (`.items()`).
- **String Methods:** `.strip()` for data cleaning and `.isdigit()` for type validation.

## How to Run

1. Make sure you have **Python 3** installed on your system.
2. Clone this repository or download the code file.
3. Open your terminal or command prompt, navigate to the project folder, and run:

```bash
python contact_book.py
