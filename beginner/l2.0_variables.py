"""
Lesson 2.0: Variables

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""

"""
Variables are a way for us to store a value for later use. Variables can be used to store (or 
technically speaking, reference / point) to data we need to save for sometime.
"""

variable_example = 123

print(variable_example)  # Prints "123".

"""
Variables are assigned by using the "=" sign followed by the value, in the previous example the 
value is "123".

As suggested earlier, we can also use them to use them for later, for example...
"""

variable_example = 100

print(variable_example)  # Prints "100".

"""
Above we can see that we can call variables multiple times and modify their value. Furthermore, we 
can use the variable to contribute to setting the value of another variable.
"""

wow = 0.456

total = variable_example + wow

print(total)  # Prints "100.456".
