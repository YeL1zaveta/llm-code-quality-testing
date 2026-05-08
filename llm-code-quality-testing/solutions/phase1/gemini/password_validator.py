import re


def is_valid_password(password):
    if not isinstance(password, str):
        return False

    if len(password) < 8:
        return False

    if ' ' in password:
        return False

    # Check for: uppercase, lowercase, digit, and special character
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    return all([has_upper, has_lower, has_digit, has_special])