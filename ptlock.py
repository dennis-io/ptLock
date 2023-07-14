import argparse
import string
import secrets
import configparser
import os
import sys
import pyperclip
import random

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True, exclude_chars=''):
    character_sets = []
    if include_uppercase:
        character_sets.append(set(string.ascii_uppercase) - set(exclude_chars))
    if include_lowercase:
        character_sets.append(set(string.ascii_lowercase) - set(exclude_chars))
    if include_digits:
        character_sets.append(set(string.digits) - set(exclude_chars))
    if include_special_chars:
        character_sets.append(set(string.punctuation) - set(exclude_chars))

    character_sets = [list(x) for x in character_sets if x]  # Remove empty lists
    if not character_sets:
        raise ValueError("At least one character set must be included.")

    password_characters = []
    for character_set in character_sets:
        password_characters.append(secrets.choice(character_set))

    while len(password_characters) < length:
        character_set = secrets.choice(character_sets)
        password_characters.append(secrets.choice(character_set))

    random_generator = random.Random()
    random_generator.seed(os.urandom(256))
    random_generator.shuffle(password_characters)
    password = ''.join(password_characters)
    return password

def parse_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def parse_arguments(config):
    parser = argparse.ArgumentParser(description='Generate a strong password.')
    parser.add_argument('-l', '--length', type=int, default=config.getint('length', 'default'), help='The length of the password')
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
