# -*- coding: UTF-8 -*-
# /**
# * Software Name : family
# * Version : 0.1.0
# *
# * Copyright 2020. PUNDIR ASHISH.
# *
# *--------------------------------------------------------
# * File Name : family/familytree.py
# * Created : 2020-06-28
# * Authors : PUNDIR ASHISH
# *--------------------------------------------------------
# */


class FamilyTree:
    """
    Family tree represent the family tree.
    contain information and functions related to the family tree.
    """

    def __init__(self, root):
        self.root = root
        self.familyMembers = {
                                root.bloodline.name: root
                            }

    def add_descendants(self, family_name, descendants):
        """
        add an descendants to the family sub tree.
        :param family: family name to add descendants.
        :param descendants: descendants to be added.
        :return:
        """
        sub_family = self.fetch_family(family_name)
        if sub_family is not None:
            sub_family.add_children(descendants)
            self.familyMembers[descendants.bloodline.name] = descendants
        else:
            return False

    def fetch_family(self, family_name):
        """
        fetch the object of family from family tree.
        :param family_name: name of family to fetch from family tree.
        :return: return family object or None
        """
        if family_name in self.familyMembers:
            return self.familyMembers[family_name]
        else:
            return None
