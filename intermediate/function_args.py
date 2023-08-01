"""
Function Arguments (args & kwargs)

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""


# ---------- ARGS ----------------------------------------------------------------------------------
# Allows passing an unknown variable number of non keyword arguments to the function.
def args_func(*args):
    total = 0

    for num in args:
        total += num

    print(f"Sum: {total}")


# ---------- KWARGS --------------------------------------------------------------------------------
# Allows passing an unknown variable number of keyword arguments to the function.
def kwarg_func(**kwargs):
    print("\nData type of argument:", type(kwargs))

    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


if __name__ == "__main__":
    args_func("Sita", "Sharma", 22, 1234567890)
    kwarg_func(
        Firstname="John",
        Lastname="Wood",
        Email="johnwood@nomail.com",
        Country="Wakanda",
        Age=25,
        Phone=9876543210,
    )
