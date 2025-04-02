# import necessary packages
import re
from datetime import datetime


# function to validate date of birth
def validate_dob(dob):
    try:
        dob_parsed = datetime.strptime(dob, "%Y-%m-%d")
        if dob_parsed > datetime.now():
            return False, "Date of birth cannot be in the future."
        return True, None
    except ValueError:
        return False, "Date of birth must be in the format YYYY-MM-DD. Example: 2001-01-01"


# function to validate phone number
def validate_phone_num(phone_num):
    if not phone_num.isdigit():
        return False, "Phone number must contain only digits."
    if len(phone_num) != 10:
        return False, "Phone number must be exactly 10 digits long."
    return True, None


# function to validate password
def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[a-zA-Z]", password):
        return False, "Password must contain at least one letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, None


# function to confirm that the password and confirm password match
def password_confirmation(password, confirm_password):
    if password != confirm_password:
        return False, "Passwords do not match."
    return True, None
