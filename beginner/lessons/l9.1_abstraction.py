"""
Lesson 9.1: Abstraction (Classes)

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""


# ---------- EXCEPTION ABSTRACTION CLASS EXAMPLE ----------
class WowCustomError(RuntimeError):  # Subclass of an error type, in this case a RuntimeError.
    def __init__(self, attribute_1):
        pass

    def __str__(self):
        return "Console Error Message"


raise WowCustomError("test")


# ---------- ABSTRACT CLASS ----------
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def abstract_method_name(self):
        # Child class is responsible for providing an implementation for the parent class's
        #  abstract method.
        pass


class AbstractSubClass(AbstractClass):
    def abstract_method_name(self):
        print("Subclass of Abstract Class's method is here!")
