"""
File Manipulation

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""


# ---------- FILE EDITING ----------
def file_read_function(file_name):
    try:
        with open(file_name, "r") as file:
            print(f"\n\tDisplaying the contents of {file_name} ...")
            print(file.read())  # read() reads the entire file as an str
            print(file.readlines())  # readlines() reads the entire file as a list (each element is a line as str)

    except FileNotFoundError:
        print(f"\n\tERROR! {file_name} does not exist!")


def file_append_function(file_name, add_data):
    try:
        with open(file_name, "a") as file:
            file.write(add_data)  # Adds to the file in append more

    except FileExistsError:
        print(f"\n\tERROR! {file_name} already exists!")


def file_create_write_function(file_name, add_data):
    try:
        with open(file_name, "w") as file:
            file.write(add_data)  # Rewrite the file completely

    except FileExistsError:
        print(f"\n\tERROR! {file_name} already exists!")
