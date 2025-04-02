# import necessary packages
from tkinter import messagebox
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel
from database_operations import register_user, find_user_with_phone, update_user_data, delete_user_with_phone
from validation import validate_dob, validate_phone_num, validate_password, password_confirmation

# set up the application window
app = CTk()
app.title("User Account Registration")
app.geometry("650x750")

# defining global variables for entries
user_first_name = None
user_last_name = None
user_dob = None
user_phone_num = None
user_password = None
confirm_user_password = None
user_address = None
search_phone_num = None
new_user_first_name = None
new_user_last_name = None
new_user_dob = None
new_user_phone_num = None
new_user_password = None
new_user_address = None

# pre defining styles
button_style = {
   "corner_radius": 30,
   "width": 175,
   "height": 27,
   "font": ("Aptos", 14)
}

label_style = {
   "font": ("Aptos", 14)
}

text_style = {
   "width": 300,
   "font": ("Aptos", 14)
}


# register new user form
def register_form():
    clear_screen()
    global user_first_name, user_last_name, user_dob, user_phone_num, user_password, confirm_user_password, user_address
   
    CTkLabel(app, text="Register New User", font=("Aptos", 25)).pack(pady=20)
   
    CTkLabel(app, text="First Name:", **label_style).pack()
    user_first_name = CTkEntry(app, **text_style)
    user_first_name.pack(pady=5)
   
    CTkLabel(app, text="Last Name:", **label_style).pack()
    user_last_name = CTkEntry(app, **text_style)
    user_last_name.pack(pady=5)
   
    CTkLabel(app, text="Date of Birth (YYYY-MM-DD):", **label_style).pack()
    user_dob = CTkEntry(app, **text_style)
    user_dob.pack(pady=5)
   
    CTkLabel(app, text="Phone Number:", **label_style).pack()
    user_phone_num = CTkEntry(app, **text_style)
    user_phone_num.pack(pady=5)
   
    CTkLabel(app, text="Password:", **label_style).pack()
    user_password = CTkEntry(app, show="*", **text_style)
    user_password.pack(pady=5)

    CTkLabel(app, text="Password must be at least 8 characters,\ninclude letters, numbers, and special characters.",
             **label_style).pack(pady=(0, 5))
   
    CTkLabel(app, text="Confirm Password:", **label_style).pack()
    confirm_user_password = CTkEntry(app, show="*", **text_style)
    confirm_user_password.pack(pady=5)
   
    CTkLabel(app, text="Address:", **label_style).pack()
    user_address = CTkEntry(app, **text_style)
    user_address.pack(pady=5)
   
    CTkButton(app, text="Register", command=register_new_user, **button_style).pack(pady=10)
    CTkButton(app, text="Back to Menu", command=show_menu, **button_style).pack(pady=10)


# validating user input and updating the database
def register_new_user():
    first_name = user_first_name.get()
    last_name = user_last_name.get()
    dob = user_dob.get()
    phone_num = user_phone_num.get()
    password = user_password.get()
    confirm_password = confirm_user_password.get()
    address = user_address.get()
   
    missing_fields = []
    if not first_name:
        missing_fields.append("First Name")
    if not last_name:
        missing_fields.append("Last Name")
    if not dob:
        missing_fields.append("Date of Birth")
    if not phone_num:
        missing_fields.append("Phone Number")
    if not password:
        missing_fields.append("Password")
    if not address:
        missing_fields.append("Address")
   
    if missing_fields:
        messagebox.showerror("Error", f"The following fields are required: {', '.join(missing_fields)}")
        return
   
    is_valid, error = validate_dob(dob)
    if not is_valid:
        messagebox.showerror("Invalid date of birth", error)
        return
   
    is_valid, error = validate_phone_num(phone_num)
    if not is_valid:
        messagebox.showerror("Invalid phone number", error)
        return
   
    is_valid, error = validate_password(password)
    if not is_valid:
        messagebox.showerror("Invalid password", error)
        return
   
    is_valid, error = password_confirmation(password, confirm_password)
    if not is_valid:
        messagebox.showerror("Error", error)
        return
   
    success, error = register_user(first_name, last_name, dob, phone_num, password, address)
    if success:
        messagebox.showinfo("Success", "User successfully registered!")
        show_menu()
    else:
        messagebox.showerror("Error", error)


# form to find user with phone number
def find_user():
    clear_screen()
    global search_phone_num
   
    CTkLabel(app, text="Find User", font=("Aptos", 25)).pack(pady=20)
   
    CTkLabel(app, text="Search by Phone Number:", **label_style).pack()
    search_phone_num = CTkEntry(app, **text_style)
    search_phone_num.pack(pady=5)
   
    CTkButton(app, text="Find User", command=display_user_info, **button_style).pack(pady=10)
    CTkButton(app, text="Back to Menu", command=show_menu, **button_style).pack(pady=10)


# validate phone number and display user information
def display_user_info():
    phone_num = search_phone_num.get()
   
    is_valid, error = validate_phone_num(phone_num)
    if not is_valid:
        messagebox.showerror("Invalid Phone Number", error)
        return
   
    user = find_user_with_phone(phone_num)
    if user:
        clear_screen()
        CTkLabel(app, text="User Information", **label_style).pack(pady=20)
      
        CTkLabel(app, text=f"First Name: {user[1]}", **label_style).pack()
        CTkLabel(app, text=f"Last Name: {user[2]}", **label_style).pack()
        CTkLabel(app, text=f"Date of Birth: {user[3]}", **label_style).pack()
        CTkLabel(app, text=f"Phone Number: {user[4]}", **label_style).pack()
        CTkLabel(app, text=f"Address: {user[6]}", **label_style).pack()
      
        CTkButton(app, text="Back to Menu", command=show_menu, **button_style).pack(pady=10)
    else:
        messagebox.showerror("Error", "User does not exist.")


# form to find the user to edit with phone number
def find_user_to_edit():
    clear_screen()
    global search_phone_num
    
    CTkLabel(app, text="Edit User Information", font=("Aptos", 25)).pack(pady=20)
   
    CTkLabel(app, text="Search by Phone Number:", **label_style).pack()
    search_phone_num = CTkEntry(app, **text_style)
    search_phone_num.pack(pady=5)
   
    CTkButton(app, text="Find User", command=find_user_for_edit, **button_style).pack(pady=10)
    CTkButton(app, text="Back to Menu", command=show_menu, **button_style).pack(pady=10)


# check if user exists to edit
def find_user_for_edit():
    phone_num = search_phone_num.get()
   
    is_valid, error = validate_phone_num(phone_num)
    if not is_valid:
        messagebox.showerror("Invalid Phone Number", error)
        return
   
    user = find_user_with_phone(phone_num)
    if user:
        edit_user_form(user)
    else:
        messagebox.showerror("Error", "User does not exist.")


# edit user form
def edit_user_form(user):
    clear_screen()
    global new_user_first_name, new_user_last_name, new_user_dob, new_user_phone_num, new_user_password, new_user_address
   
    CTkLabel(app, text="Edit User Information", font=("Aptos", 25)).pack(pady=20)
   
    CTkLabel(app, text="New First Name:", **label_style).pack()
    new_user_first_name = CTkEntry(app, **text_style)
    new_user_first_name.pack(pady=5)
    new_user_first_name.insert(0, user[1])
   
    CTkLabel(app, text="New Last Name:", **label_style).pack()
    new_user_last_name = CTkEntry(app, **text_style)
    new_user_last_name.pack(pady=5)
    new_user_last_name.insert(0, user[2])
   
    CTkLabel(app, text="New Date of Birth (YYYY-MM-DD):", **label_style).pack()
    new_user_dob = CTkEntry(app, **text_style)
    new_user_dob.pack(pady=5)
    new_user_dob.insert(0, user[3])
   
    CTkLabel(app, text="New Phone Number:", **label_style).pack()
    new_user_phone_num = CTkEntry(app, **text_style)
    new_user_phone_num.pack(pady=5)
    new_user_phone_num.insert(0, user[4])
   
    CTkLabel(app, text="New Password:", **label_style).pack()
    new_user_password = CTkEntry(app, show="*", **text_style)
    new_user_password.pack(pady=5)
    new_user_password.insert(0, user[5])

    CTkLabel(app, text="Password must be at least 8 characters,\ninclude letters, numbers, and special characters.",
             **label_style).pack(pady=(0, 5))
   
    CTkLabel(app, text="New Address:", **label_style).pack()
    new_user_address = CTkEntry(app, **text_style)
    new_user_address.pack(pady=5)
    new_user_address.insert(0, user[6])
   
    CTkButton(app, text="Update Information", command=lambda: update_user(user[4]), **button_style).pack(pady=10)
    CTkButton(app, text="Back to Menu", command=show_menu, **button_style).pack(pady=10)


# validate user input and updating the database
def update_user(old_phone_num):
    new_first_name = new_user_first_name.get()
    new_last_name = new_user_last_name.get()
    new_dob = new_user_dob.get()
    new_phone_num = new_user_phone_num.get()
    new_password = new_user_password.get()
    new_address = new_user_address.get()
   
    missing_fields = []
    if not new_first_name:
        missing_fields.append("First Name")
    if not new_last_name:
        missing_fields.append("Last Name")
    if not new_dob:
        missing_fields.append("Date of Birth")
    if not new_phone_num:
        missing_fields.append("Phone Number")
    if not new_password:
        missing_fields.append("Password")
    if not new_address:
        missing_fields.append("Address")
   
    if missing_fields:
        messagebox.showerror("Error", f"The following fields are required: {', '.join(missing_fields)}")
        return
   
    is_valid, error = validate_dob(new_dob)
    if not is_valid:
        messagebox.showerror("Invalid date of birth", error)
        return
   
    is_valid, error = validate_phone_num(new_phone_num)
    if not is_valid:
        messagebox.showerror("Invalid phone number", error)
        return
   
    is_valid, error = validate_password(new_password)
    if not is_valid:
        messagebox.showerror("Invalid password", error)
        return
   
    success, error = update_user_data(new_first_name, new_last_name, new_dob, new_phone_num, new_password, new_address,
                                      old_phone_num)
    if success:
        messagebox.showinfo("Success", "User information updated successfully!")
        show_menu()
    else:
        messagebox.showerror("Error", error)


# form to delete user with phone number
def delete_user_form():
    clear_screen()
    global search_phone_num
   
    CTkLabel(app, text="Delete User", font=("Aptos", 25)).pack(pady=20)
   
    CTkLabel(app, text="Search by Phone Number:", **label_style).pack()
    search_phone_num = CTkEntry(app, **text_style)
    search_phone_num.pack(pady=5)
   
    CTkButton(app, text="Delete User", command=delete_user, **button_style).pack(pady=10)
    CTkButton(app, text="Back to Menu", command=show_menu, **button_style).pack(pady=10)


# validate the phone number and delete the user from the database
def delete_user():
    phone_num = search_phone_num.get()
   
    is_valid, error = validate_phone_num(phone_num)
    if not is_valid:
        messagebox.showerror("Invalid Phone Number", error)
        return
   
    user = find_user_with_phone(phone_num)
    if user:
        confirm = messagebox.askokcancel(
           "Confirm Deletion",
           f"Press OK to confirm deletion of user?\n\n"
           f"First Name: {user[1]}\n"
           f"Last Name: {user[2]}\n"
           f"Date of Birth: {user[3]}\n"
           f"Phone Number: {user[4]}\n"
           f"Address: {user[6]}\n\n"
           f"Do you want to delete this user?"
        )
        if confirm:
            delete_user_with_phone(phone_num)
            messagebox.showinfo("Success", "User deleted successfully!")
            show_menu()
    else:
        messagebox.showerror("Error", "User does not exist.")


# clears all widgets one by one for new widgets
def clear_screen():
    for widget in app.winfo_children():
        widget.destroy()
       
       
# main menu buttons
def show_menu():
    clear_screen()
    CTkLabel(app, text="User Account Registration", font=("Aptos", 30)).pack(pady=20)
    CTkButton(app, text="Register New User", command=register_form, **button_style).pack(pady=10)
    CTkButton(app, text="Find User", command=find_user, **button_style).pack(pady=10)
    CTkButton(app, text="Edit User Information", command=find_user_to_edit, **button_style).pack(pady=10)
    CTkButton(app, text="Delete User", command=delete_user_form, **button_style).pack(pady=10)
    CTkButton(app, text="Exit", command=app.quit, **button_style).pack(pady=10)


# when run, it shows the main menu first
show_menu()
app.mainloop()
