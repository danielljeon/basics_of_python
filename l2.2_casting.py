"""
Lesson 2.2: Casting

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""


int_example = -64

"""
Sometimes we need to be able to convert variables from one data type to another. We can do this 
through "casting". For example, when we convert a int value to a float we say we are "casting" an 
int value to float, or int is "cast" to "float".
"""

print(int_example)  # Prints "-64", which is the original int representation.

print(float(int_example))  # Prints "-64.0" which is the in value cast to float.

"""
Of course, we can do this to assign values to a variable as well...
"""

int_to_str = str(int_example)
print(int_to_str)
