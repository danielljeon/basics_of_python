def list_comprehension():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    new_list = [x for x in fruits if "a" in x]  # List is made of -> For each element in iterable, if "a" in iterable

    print(new_list)


def list_comprehension_equivalent():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    new_list = []

    for x in fruits:
        if "a" in x:
            new_list.append(x)

    print(new_list)
