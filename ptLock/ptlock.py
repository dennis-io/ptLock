import argparse
import string
import secrets
import configparser
import os
import sys
import pyperclip
import random
import time

def parse_config():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, 'config.ini')

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True, exclude_chars=''):
    if length <= 0:
        raise ValueError("Password length must be a positive integer.")

    character_set = []

    if include_uppercase:
        character_set.extend(char for char in string.ascii_uppercase if char not in exclude_chars)
    if include_lowercase:
        character_set.extend(char for char in string.ascii_lowercase if char not in exclude_chars)
    if include_digits:
        character_set.extend(char for char in string.digits if char not in exclude_chars)
    if include_special_chars:
        character_set.extend(char for char in string.punctuation if char not in exclude_chars)

    if not character_set:
        raise ValueError("At least one character set must be included.")

    password_characters = [secrets.choice(character_set) for _ in range(length)]
    random.shuffle(password_characters)
    password = ''.join(password_characters)

    return password

def validate_length(input_length, min_length):
    if input_length < min_length:
        print(f"⚠️ The password length you provided ({input_length}) is less than the minimum ({min_length}).")
        print("💡 For better security, the minimum password length has been set to the minimum length.")
        return min_length
    return input_length

def validate_character_set(char_set):
    valid_chars = {'u', 'l', 'd', 's'}
    if not set(char_set).issubset(valid_chars):
        print(f"⚠️ Invalid character set provided ({char_set}). Only 'u', 'l', 'd', 's' are allowed.")
        print("🔧 Using default character set 'ulds'.")
        return 'ulds'
    return char_set

def parse_arguments(config):
    parser = argparse.ArgumentParser(description='Generate a strong password.')
    parser.add_argument('-l', '--length', type=int, default=config.getint('length', 'default', fallback=12),
                        help='The length of the password. Must be a positive integer. Default is 12 or the value specified in the config file.')
    parser.add_argument('-s', '--sets', type=str, default=config.get('sets', 'include_sets', fallback='ulds'),
                        help='Sets of characters to include in the password. Can include any combination of u (uppercase), l (lowercase), d (digits), s (special characters). Default is ulds or the value specified in the config file.')
    parser.add_argument('-e', '--exclude', type=str, default=config.get('exclusions', 'exclude_chars'),
                        help='Exclude specific characters from the password. Characters should be provided as a string. Default is no exclusions or the value specified in the config file.')
    parser.add_argument('-c', '--copy', action='store_true',
                        help='Copy the password to clipboard. The password will be available in the clipboard after running the script.')
    return parser.parse_args()

def main():
    config = parse_config()
    args = parse_arguments(config)

    min_length = config.getint('length', 'min_length', fallback=12)
    length = validate_length(args.length, min_length)
    char_set = validate_character_set(args.sets)

    try:
        password = generate_password(length, 'u' in char_set, 'l' in char_set, 'd' in char_set, 's' in char_set, args.exclude)
        print("🎉 Generated Password:", password)
        if args.copy:
            pyperclip.copy(password)
            print("📋 Password copied to clipboard.")
            time.sleep(2)  # Delay to ensure the clipboard is not cleared immediately
    except ValueError as e:
        print("❗️", str(e))

if __name__ == '__main__':
    main()
