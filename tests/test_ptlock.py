import string
from ptLock.ptlock import generate_password

def test_generate_password_length():
    length = 16
    password = generate_password(length)
    assert len(password) == length

def test_generate_password_contents():
    length = 16
    password = generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True)
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)
