# -*- coding: UTF-8 -*-
# /**
# * Software Name : family
# * Version : 0.1.0
# *
# * Copyright 2020. PUNDIR ASHISH.
# *
# *--------------------------------------------------------
# * File Name : familyapi.py
# * Created : 2020-06-28
# * Authors : PUNDIR ASHISH
# *--------------------------------------------------------
# */

from src.family import familytree, person, family


def create_family_tree(head, spouse, head_is_male=True):
    """
    To create the family tree
    :param person: take name for family person.
    :param spouse: take spouse  name for the person.
    :param head_is_male: flag to tell the head of family is male. default True
    :return: familytree object.
    """
    if head_is_male:
        head = person.Person(name=head, sex=person.sex.male, parent=None)
        spouse = person.Person(name=spouse, sex=person.sex.female, parent=None)
    else:
        head = person.Person(name=head, sex=person.sex.female, parent=None)
        spouse = person.Person(name=spouse, sex=person.sex.male, parent=None)
    root_family = family.Family(head, spouse, parent=None)
    return familytree.FamilyTree(root_family)


def addChildren(rootFamily):
    """
    Create a family tree structure.
    :param rootFamily: object of family class.
    :return: family tree object.
    """
    return familytree.FamilyTree(rootFamily)
