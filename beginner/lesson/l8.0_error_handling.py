"""
Lesson 8.0: Error Handling

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""


# ---------- TRY CATCH ----------
try:
    pass
except NameError:
    pass
except Exception as e:
    print(e)
finally:
    pass

# ---------- ASSERT ----------
temp_var = 10
assert temp_var == 10, NameError  # x must be 10, else NameError
if temp_var != 10:
    raise NameError

# ---------- INSTANCE ----------
var1 = 1

if isinstance(var1, int):  # if var1 is an instance of a int datatype ...
    pass
