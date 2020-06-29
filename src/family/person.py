# -*- coding: UTF-8 -*-
# /**
# * Software Name : family
# * Version : 0.1.0
# *
# * Copyright 2020. PUNDIR ASHISH.
# *
# *--------------------------------------------------------
# * File Name : family/family.py
# * Created : 2020-06-28
# * Authors : PUNDIR ASHISH
# *--------------------------------------------------------
# */
from src.family.constants import Sex


class Person:
    """Person class contains variables and function relating to person. """

    def __init__(self, name, sex, parent):
        self.name = name
        self.sex = sex
        self.parent = parent

    def is_boy(self):
        """
        Check if the person is boy or not.
        return, True if it is boy , else false
        """
        return self.sex == Sex.male

    def is_girl(self):
        """
        Check if the person is girl or not.
        return, True if it is girl , else false
        """
        return self.sex == Sex.female


class Male(Person):
    """Male class to create the Boy ,
       have function relating to Boy
    """

    def __init__(self, name, parent):
        Person.__init__(self, name, Sex.male, parent)


class Female(Person):
    """Male class to create the Boy ,
       have function relating to Boy
    """

    def __init__(self, name, parent):
        Person.__init__(self, name, Sex.female, parent)