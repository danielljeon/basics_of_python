"""
Lesson 5.0: Iterables

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""

"""
The term "iterables" or "iterable" refers to an object that is a set of smaller elements within. An 
example we've already covered are strings, a string is really just a set of characters. To move 
through the string we say that we "iterate" through the string. Iteration is is a key fundamental 
aspect we will cover in later lessons. Here we will be discussing common types of iterable data 
types that are important to know. 
"""

# ---------- Declaration ---------------------------------------------------------------------------
list_example = [1, 2, "abc", 3, 1]  # List (list): uses square [] brackets.
set_example = {1, 2, "abc", 3, 1}  # Set (set): uses curly {} brackets.
tuple_example = (1, 2, "abc", 3, 1)  # Tuple (tuple): uses round () brackets.

# ---------- Duplicate Behaviour -------------------------------------------------------------------
print(list_example)  # Prints "[1, 2, 'abc', 3, 1]".
print(set_example)  # Prints "{'abc', 1, 2, 3}".
print(tuple_example)  # Prints "(1, 2, 'abc', 3, 1)".

"""
Notice here that sets do not allow for duplicates. Although 2 elements of value 1 were declared 
initially, after the set is created duplicates are removed. This is especially helpful when we need 
to remove duplicates from a list, this would be done with a cast to set.
"""

grocery_list = ["apples", "bananas", "apples", "3 Sardaukar battalions"]
print(grocery_list)  # Prints "['apples', 'bananas', 'apples', '3 Sardaukar battalions']".
print(set(grocery_list))  # Prints "{'3 Sardaukar battalions', 'apples', 'bananas'}".

# ---------- Mutable Behaviour ---------------------------------------------------------------------
# To add or remove single elements to the aforementioned datatypes, we use the functions seen below.
list_example.append("spice")  # Add "spice" using the append function.
list_example.remove("abc")  # Remove "abc" using the remove function.

set_example.add("spice")  # Add "spice" using the add function.
set_example.remove("abc")  # Remove "abc" using the remove function.

"""
Note that list and set data types can be modified as they are deemed "mutable". However tuples are 
"immutable" meaning they cannot be modified after declaration.
"""

# tuple_example.append("spice")
# tuple_example.add("spice")
# tuple_example.remove("abc")

# ---------- Sorting behaviour ---------------------------------------------------------------------
