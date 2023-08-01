"""
Lesson 6.0: Loops

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""

# ---------- LOOPS ----------
list_example = [1, 2, 3]

for i in range(len(list_example)):  # for loop example
    break

for _ in range(10):  # for _ means ignore the current element
    break

while True:  # while loop example
    break

# ---------- ENUMERATE ----------
some_iterable = []
enumerate(some_iterable, start=0)

"""
some_iterable - something that is iterable
start - is the position in the iterator from where the counting starts. (Default is 0)
"""

for i in range(5):
    pass
