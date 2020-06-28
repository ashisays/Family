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
        self.familyMembers = {}
