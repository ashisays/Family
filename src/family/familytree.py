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
        self.familyMap = {
            root.family_head.name: root
        }

    def add_descendants(self, family_name, descendants):
        """
        add an descendants to the family sub tree.
        :param family_name: family name to add descendants.
        :param descendants: descendants to be added.
        :return:
        """
        # fetch teh family from the family tree
        sub_family = self.fetch_family(family_name)
        # check if sub_family is found or not.
        if sub_family is None:
            # if subfamily is not found in family tree return false
            return False
            # if add children failed, return false
        if not sub_family.add_children(descendants):
            return False
        # add children name to family instance to the family map
        self.familyMap[descendants.family_head.name] = descendants
        return True

    def fetch_family(self, family_name):
        """
        fetch the object of family from family tree.
        :param family_name: name of family to fetch from family tree.
        :return: return family object or None
        """
        # check if family_name is present in the family map or not.
        if family_name in self.familyMap:
            # return family if found
            return self.familyMap[family_name]
        else:
            # return None if not found
            return None

    def add_descendants_spouse(self, family_name, spouse):
        """
        add an descendants to the family sub tree.
        :param family_name: family name to add descendants.
        :param descendants: descendants to be added.
        :return:
        """
        # fetch the family from the family tree
        sub_family = self.fetch_family(family_name)
        # check if family is present or not.
        if sub_family is None:
            return False
        # if family is found add spouse to family name
        if not sub_family.add_spouse(spouse):
            return False
        # if spouse is added to the correctly return true.
        self.familyMap[spouse.name] = sub_family
        return True

