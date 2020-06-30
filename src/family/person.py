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
        self._childs = []

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
        :return: True if succeed else False
        """
        if self.get_sex() == spouse.get_sex() or self.is_married() or spouse.is_married():
            return False
        # if spouse is adding you as spouse. Then add it as spouse
        self._spouse = spouse
        spouse._spouse = self
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

    def add_child(self, child):
        """
        Add child to the person
        Check if child with same nams is added or not.
        :param child: child member to be added.
        :return:True if succed , else False.
        """
        if child is None:
            return False
        # check if child with same name is added.
        for child_member in self.get_all_childs():
            if child_member.name == child.name:
                return False
        # update child mother and father details.
        child.father = self.get_spouse()
        child.mother = self
        self._childs.append(child)
        return True

    def get_all_childs(self):
        """
        provide list of child members related to person.
        :return: empty list or list of childrens.
        """
        return self._childs

    def get_siblings_of(self, gender, person_name):
        """
        fetch siblings of a person.
        :param gender: gender of sibling to be fetched.
        :param person_name: name of person whose siblings to be sent.
        :return: list of siblings or empty list.
        """
        gender = eval("Sex.%s" % gender)
        child_of_required_gender = []
        for child in self._childs:
            if child.get_sex() == gender and child.name is not person_name:
                child_of_required_gender.append(child)
        return child_of_required_gender

    def get_childs(self, gender):
        """
        get childs list based on the gender.
        :param gender: gender of the childs to fetch.
        :return: lsit of childs with particular gender.
        """
        gender = eval("Sex.%s" % gender)
        child_of_required_gender = []
        for child in self._childs:
            if child.get_sex() == gender:
                child_of_required_gender.append(child)
        return child_of_required_gender
