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
from src.family.constants import Sex, Message, Commands, RelationShip



class FamilyAPI:
    """
    This class representing fucntion and variables related to Family.
    From file processing to sending the commands and getting output.
    """
    def __init__(self):
        self.family = None

    def call(self, commands):
        method_name = commads[0].lower()
        method = getattr(self, method_name, lambda: 'INVALID_COMMAND')
        return method(commands[1:])

    def add_child(self,mother_name,child_name,gender):
        return self.family.add_child(mother_name,child_name,gender)

    def add_spouse(self,member_name,spouse_name,spouse_gender):
        self.family.add_spouse(member_name,spouse_name,spouse_gender)

    def add_family_head(self,family_head_name,gender):
        self.family = family.Family(family_head_name,gender)

    def get_relationship(self,relationship,person_name):
        return self.family.get_relationship(relationship,person_name)


    def process_input_file(self,family,file,inititalisation=False):
        """
        process the input file and create family or process commands.
        :param family: family name
        :param file: file to process.
        :return: True or False on success and failure respectively.
        """
        with open(file,"r") as fd:
            for command in fd.readlines():
                if inititalisation:
                    self.process_inititalisation_command(family,command)
                else:
                    self.process_input_command(family, command)

    def process_inititalisation_command(self,family,command):
        """
        process intialisaion command to create family hirearchy from the file provided.
        :param family: family to be created based on input file.
        :param command: command to be processed.
        :return:None
        """
        command_params = command.split(" ")
