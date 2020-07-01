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
import os

from src.family import  family


class FamilyAPI:
    """
    This class representing fucntion and variables related to Family.
    From file processing to sending the commands and getting output.
    """

    def __init__(self):
        self.family = None

    def call(self, commands):
        """
        call method realated to commands and return its output.
        :param commands: list of commands parameters
        :return: return output of command in use in string format.
                 return "INVALID_COMMAND if its not supported."
        """
        method_name = commands[0].lower()
        method = getattr(self, method_name, lambda args: 'INVALID_COMMAND')
        if len(commands) ==3:
            return method(commands[1],commands[2])
        else:
            return method(commands[1],commands[2],commands[3])

    def add_child(self, mother_name, child_name, gender):
        """
        method name that get called for adding a child.
        :param mother_name: mother name to add child to.
        :param child_name: child name to be added.
        :param gender: gender of child to be added.
        :return:
        """
        return self.family.add_child(mother_name, child_name, gender)

    def add_spouse(self, member_name, spouse_name, spouse_gender):
        """
        method to add spouse to a particular family member.
        :param member_name: name of family member to add spouse to.
        :param spouse_name: name of spouse to be added.
        :param spouse_gender: gender of spouse to be added.
        :return: return the status of the process in string format.
        """
        return self.family.add_spouse(member_name, spouse_name, spouse_gender)

    def add_family_head(self, family_head_name, gender):
        """
        method to initialize the family, with teh provided parameters.
        :param family_head_name: head of family name to be provided.. 
        :param gender: gender of the family head to be added.
        :return: None , create a object variable obj.family set to family.
        """
        self.family = family.Family(family_head_name, gender)

    def get_relationship(self, relationship, person_name):
        """
        method fetch results of relationship for particular member name,
        :param relationship: relationship to be fetched.
        :param person_name: name of person relating to the values to be fetched.
        :return: sting of relationsip values
        """
        return self.family.get_relationship(relationship, person_name)

    def process_input_file(self, file):
        """
        process the input file and create family or process commands.
        :param file: file to process.
        :return: True or False on success and failure respectively.
        """
        if not os.path.exists(file):
            print('File Does Not Exist')
        else:
            with open(file, 'r') as fr:
                for command in fr.readlines():
                    print(self.process_input_command(command))

    def process_input_command(self, command):
        """
        process  command to create family hirearchy from the file provided.
        :param command: command to be processed.
        :return:None
        """
        command_params = command.split(";")
        return self.call(command_params)
