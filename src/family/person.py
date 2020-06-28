"""
The file contains all the variables and function related to a person class.
"""
import enum


class sex(enum.Enum):
    """
    Sex enumeration for the person.
    values are male or female.
    """
    male = 1
    female = 2


class Person:
    """Person class contains variables and function relating to person. """

    def __init__(self, name, sex, parent):
        self.name = name
        self.sex = sex
        self.parent = parent

    def isBoy(self):
        """
        Check if the person is boy or not.
        return, True if it is boy , else false
        """
        return self.sex == sex.male

    def isGirl(self):
        """
        Check if the person is girl or not.
        return, True if it is girl , else false
        """
        return self.sex == sex.female


class Male(Person):
    """Male class to create the Boy ,
       have function relating to Boy
    """

    def __init__(self, name, parent):
        Person.__init__(self, name, sex.male, parent)


class Female(Person):
    """Male class to create the Boy ,
       have function relating to Boy
    """

    def __init__(self, name, parent):
        Person.__init__(self, name, sex.female, parent)