from setuptools import setup, find_packages

setup(
    name="test_package",
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'myproject = wrapper.wrapper:main',  # if you have a main function in wrapper.py
        ],
    },
)