from setuptools import setup

setup(
    name='ptlock',
    version='1.0.0',
    description='Password generator with CLI support',
    author='neutron',
    author_email='hello@neutronsec.com',
    url='https://github.com/neutronsec/ptlock',
    packages=['ptlock'],
    install_requires=['pyperclip==1.8.2'],
    entry_points={
        'console_scripts': [
            'ptlock=ptlock.ptlock:main',
        ],
    },
)
