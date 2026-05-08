#from solutions.phase1.grok.password_validator import is_valid_password
#from solutions.phase1.claude.password_validator import is_valid_password
#from solutions.phase1.chatgpt.password_validator import is_valid_password
from solutions.phase1.gemini.password_validator import is_valid_password


#from solutions.phase2.grok.password_validator import is_valid_password
#from solutions.phase2.claude.password_validator import is_valid_password
#from solutions.phase2.chatgpt.password_validator import is_valid_password
#from solutions.phase2.gemini.password_validator import is_valid_password

def test_valid_password():
    assert is_valid_password("Abc123!@") == True

def test_valid_password_another1():
    assert is_valid_password("Password1!") == True

def test_valid_password_another2():
    assert is_valid_password("XyZ987#@") == True

def test_no_uppercase():
    assert is_valid_password("abc123!@") == False

def test_no_lowercase():
    assert is_valid_password("ABC123!@") == False

def test_short_password1():
    assert is_valid_password("a1") == False

def test_short_password2():
    assert is_valid_password("Abc123!") == False

def test_no_numbers():
    assert is_valid_password("abc!@") == False

def test_no_special_characters():
    assert is_valid_password("abc123") == False

def test_password_with_space():
    assert is_valid_password(" Abc123!@ ") == False

def test_password_with_space_in_the_middle():
    assert is_valid_password("Abc 123!@") == False

def test_spaces():
    assert is_valid_password("    ") == False

def test_password_none():
    assert is_valid_password("") == False

def test_other_data():
    assert is_valid_password(None) == False