import pytest
from ptlock.ptlock import generate_password

def test_generate_password_length():
    password = generate_password(12)
    assert len(password) == 12

def test_generate_password_exclusion():
    password = generate_password(16, exclude_chars='abc')
    assert not any(char in password for char in 'abc')
