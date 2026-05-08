import string

def is_valid_password(password):
    if not isinstance(password, str) or password is None:
        return False

    if len(password) < 8:
        return False

    if ' ' in password:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    return all([has_upper, has_lower, has_digit, has_special])