import unittest
import string   # Add this line
from ptLock import ptlock  # adjust the import based on your package structure

class TestPtLock(unittest.TestCase):

    def test_length(self):
        for length in [1, 12, 100, 1000]:
            with self.subTest(length=length):
                password = ptlock.generate_password(length)
                self.assertEqual(len(password), length)

    def test_character_inclusion(self):
        for include_uppercase, include_lowercase, include_digits, include_special_chars in [(True, False, False, False), (False, True, False, False), (False, False, True, False), (False, False, False, True)]:
            with self.subTest(include_uppercase=include_uppercase, include_lowercase=include_lowercase, include_digits=include_digits, include_special_chars=include_special_chars):
                password = ptlock.generate_password(100, include_uppercase, include_lowercase, include_digits, include_special_chars)
                if include_uppercase:
                    self.assertTrue(any(char.isupper() for char in password))
                if include_lowercase:
                    self.assertTrue(any(char.islower() for char in password))
                if include_digits:
                    self.assertTrue(any(char.isdigit() for char in password))
                if include_special_chars:
                    self.assertTrue(any(char in string.punctuation for char in password))

    def test_character_exclusion(self):
        for exclude_chars in ['abc', '123', '!@#', 'ABC']:
            with self.subTest(exclude_chars=exclude_chars):
                password = ptlock.generate_password(100, exclude_chars=exclude_chars)
                self.assertTrue(all(char not in exclude_chars for char in password))

    def test_all_character_sets_excluded(self):
        with self.assertRaises(ValueError):
            ptlock.generate_password(12, include_uppercase=False, include_lowercase=False, include_digits=False, include_special_chars=False)

if __name__ == '__main__':
    unittest.main()
