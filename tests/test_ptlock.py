import unittest
from ptLock import ptlock

class TestPtLock(unittest.TestCase):

    def test_generate_password_length(self):
        password = ptlock.generate_password(16)
        self.assertEqual(len(password), 16)

    def test_generate_password_no_uppercase(self):
        password = ptlock.generate_password(16, include_uppercase=False)
        self.assertTrue(all(not char.isupper() for char in password))

    def test_generate_password_no_lowercase(self):
        password = ptlock.generate_password(16, include_lowercase=False)
        self.assertTrue(all(not char.islower() for char in password))

    def test_generate_password_no_digits(self):
        password = ptlock.generate_password(16, include_digits=False)
        self.assertTrue(all(not char.isdigit() for char in password))

    def test_generate_password_no_special_chars(self):
        password = ptlock.generate_password(16, include_special_chars=False)
        self.assertTrue(all(char.isalnum() for char in password))

    def test_generate_password_exclude_chars(self):
        excluded_chars = 'abc'
        password = ptlock.generate_password(16, exclude_chars=excluded_chars)
        self.assertTrue(all(char not in excluded_chars for char in password))

if __name__ == '__main__':
    unittest.main()
