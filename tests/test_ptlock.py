import unittest
import string
from ptLock import ptlock 

class TestPtLock(unittest.TestCase):

    def test_length(self):
        for length in [1, 12, 100, 1000]:
            with self.subTest(length=length):
                password = ptlock.generate_password(max(12, length))
                self.assertEqual(len(password), max(12, length))

    def test_character_inclusion(self):
        for sets in ['u', 'l', 'd', 's', 'ul', 'ud', 'us', 'ld', 'ls', 'ds', 'uld', 'uls', 'uds', 'lds', 'ulds']:
            with self.subTest(sets=sets):
                password = ptlock.generate_password(100, 'u' in sets, 'l' in sets, 'd' in sets, 's' in sets)
                if 'u' in sets:
                    self.assertTrue(any(char.isupper() for char in password))
                if 'l' in sets:
                    self.assertTrue(any(char.islower() for char in password))
                if 'd' in sets:
                    self.assertTrue(any(char.isdigit() for char in password))
                if 's' in sets:
                    self.assertTrue(any(char in string.punctuation for char in password))

    def test_character_exclusion(self):
        for exclude_chars in ['abc', '123', '!@#', 'ABC']:
            with self.subTest(exclude_chars=exclude_chars):
                password = ptlock.generate_password(100, exclude_chars=exclude_chars)
                self.assertTrue(all(char not in exclude_chars for char in password))

    def test_all_character_sets_excluded(self):
        with self.assertRaises(ValueError):
            ptlock.generate_password(12, include_uppercase=False, include_lowercase=False, include_digits=False, include_special_chars=False)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            ptlock.generate_password(-1)  # Length of password can't be negative
        with self.assertRaises(ValueError):
            ptlock.generate_password(0)   # Length of password can't be zero

if __name__ == '__main__':
    unittest.main()
