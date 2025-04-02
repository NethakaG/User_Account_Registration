# import necessary packages
import sqlite3

# creating a database connection
conn = sqlite3.connect("user_account_registration.db", isolation_level=None)
cursor = conn.cursor()

# create users table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    address TEXT
)
""")


# database operation to register a new user
def register_user(first_name, last_name, dob, phone_num, password, address):
    try:
        with conn:
            cursor.execute("""
                INSERT INTO users (first_name, last_name, dob, phone, password, address)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (first_name, last_name, dob, phone_num, password, address))
        return True, None
    except sqlite3.IntegrityError:
        return False, "A user with this phone number already exists."
    except Exception as e:
        return False, str(e)


# database operation to find a user by phone number
def find_user_with_phone(phone_num):
    cursor.execute("SELECT * FROM users WHERE phone = ?", (phone_num,))
    return cursor.fetchone()


# database operation to update user information
def update_user_data(first_name, last_name, dob, phone_num, password, address, old_phone_num):
    try:
        with conn:
            cursor.execute("""
                UPDATE users
                SET first_name = ?, last_name = ?, dob = ?, phone = ?, password = ?, address = ?
                WHERE phone = ?
            """, (first_name, last_name, dob, phone_num, password, address, old_phone_num))
        return True, None
    except Exception as e:
        return False, str(e)


# database operation to delete a user by phone number
def delete_user_with_phone(phone_num):
    cursor.execute("DELETE FROM users WHERE phone = ?", (phone_num,))
    conn.commit()
