Sure, here's the provided information formatted in markdown:

---

**To prepare your environment:**

First, install `wheel` using pip:

```
pip install wheel
```

Create a virtual environment:

```
python3 -m venv env
.\env\Scripts\activate
```

**Steps to convert Python code into a .whl package:**

1. **Setup a new project:**

Create a new directory for your project and place your Python files in it. The structure might look like this:

```
/myproject
    /myproject
        __init__.py
        wrapper.py
    setup.py
```

2. **Create a setup.py file:**

This file is required for packaging and should contain information about your package. Here's a basic example:

```python
from setuptools import setup, find_packages

setup(
    name='myproject',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'myproject = myproject.wrapper:main',  # if you have a main function in wrapper.py
        ],
    },
)
```

3. **Generate the distribution package:**

Run the following command in your terminal:

```
python setup.py bdist_wheel
```

**How to setup and run a .whl file in your local system:**

To install and run a .whl file in your local system, follow these steps:

1. **Install the wheel file:**

You can install a .whl file using pip. Navigate to the directory containing the .whl file and run the following command:

```
pip install myproject-0.1-py3-none-any.whl
```

Replace `myproject-0.1-py3-none-any.whl` with the name of your .whl file.

2. **Run the installed package:**

If your package contains an executable script (defined in entry_points in setup.py), you can run it directly from the command line:

```
myproject
```

Replace `myproject` with the name of your script.

Please note that you might need to use `python -m pip install ...` instead of `pip install ...` if you have multiple Python versions installed. Also, it's a good practice to install packages in a virtual environment to avoid conflicts with system-wide packages.


---

To use the installed package `test_package-0.1`, you can import it in your Python script. However, the import statement should use the package name, not the distribution name. In this case, the package name is [package_test](file:///c%3A/Users/dasik/Desktop/whl_file/readme.md#89%2C209-89%2C209) as indicated in the `top_level.txt` file.

Here is a simple Python script that imports and uses the package:

```python
import package_test

# Use the package here
```

Please replace `# Use the package here` with the actual usage of the package. The specific usage will depend on the functions and classes provided by the `package_test` package.

---

add all the important functions in the __init__.py file

```python
from .aes import aes_encrypt
from .caeser import caesar_encrypt

```

---

import the library and test

```python

import package_test
data = "hello world"
shift = 3

encrypted_data_aes = package_test.aes_encrypt(data)
encrypted_data_caesar = package_test.caesar_encrypt(data, shift)

print(encrypted_data_aes)
print(encrypted_data_caesar)
```

