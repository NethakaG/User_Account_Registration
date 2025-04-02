# User Account Registration System

This is a simple desktop app for managing user accounts. You can register new users, search for existing ones, edit their details, or delete them completely — all through a neat little GUI built with Python.

---

## What It Uses

- Python 3
- customtkinter (for the GUI)
- SQLite (for storing user data)

---

## Features

- Register users with:
  - First name, last name, DOB, phone number, password, address
- Validate:
  - DOB format and future dates
  - Phone number length and digits
  - Strong passwords (letters, numbers, symbols)
- Confirm passwords before saving
- Search for existing users using their phone number
- Edit any saved user’s information
- Delete users after confirmation
- Everything’s stored in a local SQLite `.db` file

 **Note:** This is built to work with SQLite only. It won’t connect to other databases.

---

## Project Structure

```
.
├── main.py                  # Main app with the GUI
├── validation.py            # Input validation logic
├── database_operations.py   # All database-related functions
```

---

## That’s it!

Hope this helps you or someone else learn something new. If you like it or want to build on top of it — go for it!
