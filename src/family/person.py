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

    def __init__(self, name, sex, mother=None, father=None):
        self.name = name
        self._mother = mother
        self._father = father
        self._spouse = None
        self._sex = sex
        self._child = []

    def is_boy(self):
        """
        Check if the person is boy or not.
        return, True if it is boy , else false
        """
        return Sex.male == self._sex

    def is_married(self):
        """
        :return: if the person is married or not.
        :return True if its married or false if not.
        """
        if self._spouse is not None:
            return True
        return False

    def is_girl(self):
        """
        Check if the person is girl or not.
        return, True if it is girl , else false
        """
        return self._sex == Sex.female

    def get_sex(self):
        """
        :return: return the sex of the person
        """
        return self._sex

    def get_parent_name(self):
        """return parent information."""
        return self._father.name, self._mother.name

    def get_mother(self):
        """
        return mother object from the person
        """
        return self._mother

    def get_father(self):
        """
        :return: father object for person.
        """
        return self._father

    def add_spouse(self, spouse):
        """
        add spouse to the person.
        check if gender of both is different
        :param spouse:
        :return: True if succed else False
        """
        if self.get_sex() == spouse.get_sex() or self.is_married() or spouse.is_married():
            return False
        # if spouse is adding you as spouse. Then add it as spouse
        self._spouse = spouse
        spouse.add_spouse = self
        return True

    def get_spouse(self):
        """
        return spouse to the person.
        :return: spouse if succeed else None
        """
        if self._spouse:
            return self._spouse
        return None


class Male(Person):
    """Male class to create the Boy ,
       have function relating to Boy
    """

    def __init__(self, name, mother=None, father=None):
        Person.__init__(self, name, Sex.male, mother, father)


class Female(Person):
    """Female class to create the Girl ,
       have function relating to Girl
    """

    def __init__(self, name, mother=None, father=None):
        Person.__init__(self, name, Sex.female, mother, father)

    def add_child(self,child):
        self._childs.append(child)

    def get_childs(self):
        return self._childs