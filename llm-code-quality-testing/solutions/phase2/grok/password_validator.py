def is_valid_password(password):
    if password is None or not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if ' ' in password:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?`~" for c in password)
    return has_upper and has_lower and has_digit and has_special