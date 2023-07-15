from setuptools import setup, find_packages

setup(
    name="ptLock",
    version="0.1",
    packages=find_packages(),  # Automatically find packages in current directory
    entry_points={
        'console_scripts': ['ptlock=ptLock.ptlock:main']
    },
    install_requires=[
        'click',
        'pyperclip'  # Add this line
    ],
    python_requires='>=3.6',
)
