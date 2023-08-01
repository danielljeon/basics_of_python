"""
Lesson 2.1: Data types

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""


int_example = -64  # Integer (int): an integer number (can be negative, 0 or positive).
float_example = 0.02  # Float (float): a decimal number, most closely resembles a rational number.
complex_example = 12j  # Complex (complex): a complex number where j is the imaginary.
str_example = "Abc 12.3 !@#"  # String (str): text made of various characters.
bool_example = True  # Boolean (bool): True or False.
none_example = None  # None (None): in simple terms None represents "no" value.

"""
These are just a few of the more basic data types that we can use in Python. In future lessons we 
will cover more complex data types.

Lastly, if we ever want to see what kind of data type a value is we can use the type function.
"""

print(type(int_example))
print(type(float_example))
print(type(complex_example))
print(type(str_example))
print(type(bool_example))
print(type(none_example))
