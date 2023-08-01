"""
Lesson 9.0: Object Oriented Programming (OOP)

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""


# ---------- CLASSES AND OBJECTS ----------
class ClassName:
    """
    class example with object attributes
    """

    def __init__(self, attribute1, semi_private_att, private_att, default_none=None, default_6=6):
        self.attribute1 = attribute1
        self._semi_private_att = semi_private_att  # _attribute: "weak internal use" indicator.
        self.__private_att = private_att  # __attribute: "name mangling" indicator.
        self.default_to_none = default_none
        self.default_to_6 = default_6
        """
        Name Mangling: __spam is textually replaced with _classname__spam, 
        where classname is the current class name with leading underscore(s) stripped. 
        Essentially allows privatisation of variables and attributes
        """

    # method (function in a class) example
    def method_name(self):
        return

    def get_a(self):
        return self.attribute1

    def set_a(self, att1):
        self.attribute1 = att1

    # self print str
    def __str__(self):
        return "attribute1: %s\n_semi_private_att: %d\n__private_att: %.2f" % (
            self.attribute1,
            self._semi_private_att,
            self.__private_att,
        )
        # %s = string, %d = data, %.2f = 2 decimal point float


class Subclass(ClassName):
    """
    Subclass example with subclass object attributes
    """

    def __init__(self, attribute1, semi_private_att, private_att, subclass_att, default_none=None):
        self.__subclass_att = subclass_att
        super().__init__(attribute1, semi_private_att, private_att, subclass_att, default_none)

    """
    super() will invoke the equal class of the subclass (in this case equal to ClassName class)
    """
