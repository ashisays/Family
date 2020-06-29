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
    root_family = family.Family(head, parent=None, spouse=spouse)
    return familytree.FamilyTree(root_family)


def add_descendants(rootFamily, family_name, child_name, child_sex):
    """
    Create a family tree structure.
    :param rootFamily: object of family class.
    :return: family tree object.
    """
    child = person.Person(name=child_name, sex=eval("person.sex.%s" % child_sex), parent=None)
    child_sub_family = family.Family(person=child, spouse=None, parent=None)
    return rootFamily.add_descendants(family_name, child_sub_family)


def add_spouse(rootFamily, family_name, spouse_name, spouse_sex):
    """
    Add spouse to the family, if it have single male or female.
    and sex is different for each other.
    :param rootFamily: family tree.
    :param family_name: family name to add the spouse to.
    :param spouse_name: Name of spouse to be added.
    :param spouse_sex: Sex of spouse to be added.
    :return:
    """
    spouse = person.Person(name=spouse_name, sex=eval("person.sex.%s" % spouse_sex), parent=None)
    return rootFamily.add_descendants_spouse(family_name, spouse)
