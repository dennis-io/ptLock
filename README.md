# 💪💻 ptLock: Python Turbo Lock Password Generator 🎉🔒

Welcome to ptLock! This robust Python tool generates secure, complex passwords for all your needs. Customize your passwords' length and composition, and even specify characters to exclude!

## 🚀 Getting Started

### 🖥️ Installation

1. Make sure you have Python 3.6 or higher installed. Verify your Python version by running `python --version` in your terminal.

2. Clone the ptLock repository with the following command: `git clone https://github.com/neutronsec/ptLock.git`

3. Navigate to the ptLock directory: `cd ptLock/`

4. Install ptLock and its dependencies by running: `pip install .`

### 🛠️ Configuration

ptLock uses a configuration file (`config.ini`) for default settings. You can change these defaults to suit your needs.

Here's a quick overview of the `config.ini` sections:

- `[length]`: Define the default length of the password.
- `[sets]`: Specify whether to include uppercase letters, lowercase letters, digits, and special characters.
- `[exclusions]`: Exclude specific characters from the password.

For example:

```ini
[length]
default = 16

[sets]
include_uppercase = True
include_lowercase = True
include_digits = True
include_special_chars = True

[exclusions]
exclude_chars = {}
```

### 🎯 Usage

You can run ptLock directly from the command line with various options:

```shell
ptlock -l 16 -s ulds -e "abcdef0123"
```

The options are:

- `-l` or `--length`: The length of the password.
- `-s` or `--sets`: Sets of characters to include in the password: u (uppercase), l (lowercase), d (digits), s (special characters).
- `-e` or `--exclude`: Exclude specific characters from the password.
- `-c` or `--copy`: Copy the password to clipboard.

### 💡 Tips for a Strong Password

- Make it at least 12 characters long. The longer, the better!
- Include a mix of uppercase and lowercase letters, numbers, and symbols.
- Don't use personal information or common words.
- Don't reuse passwords across multiple accounts.
- Regularly update your passwords.

### 😊 Contribution

We welcome all contributions! If you find a bug 🐛 or want to propose a new feature, please open an issue on the GitHub repository.

## 📄 License

The project is licensed under the terms of the [LICENSE](LICENSE) file.