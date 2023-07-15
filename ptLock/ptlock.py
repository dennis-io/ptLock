import argparse
import string
import secrets
import configparser
import os
import sys
import pyperclip
import random

def parse_config():
    # Get the path to the config.ini file based on the location of ptlock.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, 'config.ini')

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True, exclude_chars=''):
    # Initialize the list of possible characters
    character_set = []

    # Add the desired types of characters to the list
    if include_uppercase:
        character_set.extend(char for char in string.ascii_uppercase if char not in exclude_chars)
    if include_lowercase:
        character_set.extend(char for char in string.ascii_lowercase if char not in exclude_chars)
    if include_digits:
        character_set.extend(char for char in string.digits if char not in exclude_chars)
    if include_special_chars:
        character_set.extend(char for char in string.punctuation if char not in exclude_chars)

    # Check if the character set is empty
    if not character_set:
        raise ValueError("At least one character set must be included.")

    # Generate the password
    password_characters = [secrets.choice(character_set) for _ in range(length)]

    # Shuffle the characters
    random.shuffle(password_characters)

    # Join the characters together to form the password
    password = ''.join(password_characters)

    return password


def parse_arguments(config):
    parser = argparse.ArgumentParser(description='Generate a strong password.')
    parser.add_argument('-l', '--length', type=int, default=config.getint('length', 'default', fallback=12), help='The length of the password')
    parser.add_argument('-u', '--uppercase', action='store_true', default=config.getboolean('sets', 'include_uppercase'), help='Include uppercase letters in the password')
    parser.add_argument('-lc', '--lowercase', action='store_true', default=config.getboolean('sets', 'include_lowercase'), help='Include lowercase letters in the password')
    parser.add_argument('-d', '--digits', action='store_true', default=config.getboolean('sets', 'include_digits'), help='Include digits in the password')
    parser.add_argument('-s', '--special', action='store_true', default=config.getboolean('sets', 'include_special_chars'), help='Include special characters in the password')
    parser.add_argument('-e', '--exclude', type=str, default=config.get('exclusions', 'exclude_chars'), help='Exclude specific characters from the password')
    return parser.parse_args()

def main():
    config = parse_config()
    args = parse_arguments(config)

    if args.length < 12:
        print("❗️ Password length should be at least 12 characters.")
        sys.exit(1)

    try:
        password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special, args.exclude)
        print("🎉 Generated Password:", password)
        pyperclip.copy(password)
        print("📋 Password copied to clipboard.")
    except ValueError as e:
        print("❗️", str(e))

if __name__ == '__main__':
    main()
