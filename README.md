# Console-Based Contact Book (OOP Version)

A lightweight, robust command-line interface (CLI) application written in Python that manages a contact directory with full persistent storage and secure input validation. 

Recently refactored from a procedural approach to an **Object-Oriented Programming (OOP) Architecture** to ensure clean code principles, scalability, and loose coupling.

## Tech Stack & Key Concepts

* **Language:** Python 3
* **Data Persistence:** JSON (using Python's native `json` library)
* **Design Pattern:** Object-Oriented Programming (OOP)
  * **Encapsulation:** Grouping contact-specific properties and behaviors within a `Contact` class.
  * **Separation of Concerns:** Delegating CLI control flow, file I/O operations, and list management to the `ContactBook` coordinator class.

## Input Validation & Robustness

The application actively sanitizes and validates user inputs before appending them to the persistent storage:

| Field | Rule | Handling Method |
| :--- | :--- | :--- |
| **Name** | Cannot be empty, must contain only letters and spaces (No digits or special characters) | `.strip()` & `.replace(" ", "").isalpha()` loop |
| **Phone** | Must contain only digits | `.isdigit()` loop |
| **Email** | Must contain a valid `@` symbol | Character membership validation loop |


## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone git clone [https://github.com/UmarMujahid07/contact-book-cli.git](https://github.com/UmarMujahid07/contact-book-cli.git)
   cd CONTACT-BOOK-CLI
