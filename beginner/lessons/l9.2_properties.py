"""
Lesson 9.2: Properties

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""


class Person:
    def __init__(self, value):
        self.name = value

    @property
    # Use @abstractmethod decorator to create abstract property here
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


def main():
    p = Person(42)  # Triggers TypeError: Expected a string

    p = Person("Bob")

    print(p.name)  # Prints Bob

    p.name = 42  # Triggers TypeError: Expected a string

    del p.name  # Triggers AttributeError: Can't delete attribute


if __name__ == "__main__":
    main()
