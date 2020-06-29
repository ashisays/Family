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


class Family:
    """Class representing Family
       It can either be for type single and married.
       Single only contain one person, married contain spouse and person.
    """

    def __init__(self, person, parent, spouse=None):
        self.parent = parent
        self.bloodline = person
        self.spouse = spouse
        self.married = False
        if spouse is not None:
            self.married = True
        self.descendants = {
            "sons": {}, "daughters": {}
        }
        self.girlFamilyList = []

    def get_son_in_law(self):
        """
        return the list of male childs in the family
             ->return list of sons if found in the descendants dict.
               else return empty list.
        """
        if self.bloodline.isBoy() or self.married is False:
            return None
        else:
            return self.spouse

    def get_daughter_in_law(self):
        """
        return the list of male childs in the family
             ->return list of sons if found in the descendants dict.
               else return empty list.
        """
        if self.bloodline.isBoy() and self.married is True:
            return self.spouse
        else:
            return None

    def add_children(self, child):
        """
        Add children family to the current family.
        :param child: child , Instance of family.
        :return: True on Success, False on Failure
        """
        # check if parents is married or not.
        # the child added should be of family class.
        if self.married is False or not isinstance(child, Family):
            return False
        if child.bloodline.isBoy():
            child.parent = self
            self.descendants["sons"][child.bloodline.name] = child
        else:
            self.descendants["daughters"][child.bloodline.name] = child
        return True

    def get_sons(self):
        """
        return the list of male childs in the family
             ->return list of sons if found in the descendants dict.
               else return empty list.
        """
        print("In get sons")
        sons = []
        print(self.descendants["sons"])
        for name, descendants_family in self.descendants["sons"].items():
            if isinstance(descendants_family, Family):
                sons.append(name)
        return sons

    def get_daughters(self):
        """
        return the list of female childs in the family
            ->return list of daughters if found in the descendants dict.
              else return empty list.
        """
        daughters = []
        for name, descendants_family in self.descendants["daughters"].items():
            if isinstance(descendants_family, Family):
                daughters.append(name)
        return daughters

    def add_spouse(self, spouse):
        # check person is already married or not
        if self.married or spouse is None:
            return False
        elif spouse.sex == self.bloodline.sex:
            return False
        # set spouse with
        self.spouse = spouse
        return True
