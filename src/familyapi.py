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

from src.family import family
from src.family.constants import Message, Sex


class FamilyAPI:
    """
    This class representing fucntion and variables related to Family.
    From file processing to sending the commands and getting output.
    """

    def __init__(self):
        self.family = None

    def call(self, commands,print_result=False):
        """
        call method realated to commands and return its output.
        :param commands: list of commands parameters
        :return: return output of command in use in string format.
                 return "INVALID_COMMAND if its not supported."
        """
        method_name = commands[0].lower()
        method = getattr(self, method_name, self.invalid_cmd)
        if len(commands) == 3:
            return method(commands[1], commands[2],print_result)
        else:
            method(commands[1], commands[2], commands[3],print_result)

    def invalid_cmd(self, *args):
        """
        method to be called for default value.
        :param *args any no of input
        :return: return string "INVALID_COMMAND"
        """
        return Message.INVALID_COMMAND.value

    def add_child(self, mother_name, child_name, gender,print_result=False):
        """
        method name that get called for adding a child.
        :param mother_name: mother name to add child to.
        :param child_name: child name to be added.
        :param gender: gender of child to be added.
        :return: None print the result of child addition.
        """
        if print_result:
            print(self.family.add_child(mother_name, child_name, eval("Sex.%s" % gender)))
        else:
            return self.family.add_child(mother_name, child_name, eval("Sex.%s" % gender))

    def add_spouse(self, member_name, spouse_name, spouse_gender,print_result=False):
        """
        method to add spouse to a particular family member.
        :param member_name: name of family member to add spouse to.
        :param spouse_name: name of spouse to be added.
        :param spouse_gender: gender of spouse to be added.
        :return: none, return the status of the process in string format.
        """
        if print_result:
            print(self.family.add_spouse(member_name, spouse_name, eval("Sex.%s" % spouse_gender)))
        else:
            self.family.add_spouse(member_name, spouse_name, eval("Sex.%s" % spouse_gender))

    def add_family_head(self, family_head_name, gender,print_result=False):
        """
        method to initialize the family, with teh provided parameters.
        :param family_head_name: head of family name to be provided.. 
        :param gender: gender of the family head to be added.
        :return: None , create a object variable obj.family set to family.
        """
        if print_result:
            self.family = family.Family(family_head_name, gender)
        else:
            self.family = family.Family(family_head_name, gender)

    def get_relationship(self, person_name, relationship,print_result=False):
        """
        method fetch results of relationship for particular member name,
        :param relationship: relationship to be fetched.
        :param person_name: name of person relating to the values to be fetched.
        :return: Non print the result of relationship
        """
        if print_result:
            print(self.family.get_relationship(relationship, person_name))
        else:
            return self.family.get_relationship(relationship, person_name)

    def process_input_file(self, file, print_result=False):
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
                    command = command.replace('-', '_')
                    self.process_input_command(command, print_result)


    def process_input_command(self, command,print_result=False):
        """
        process  command to create family hirearchy from the file provided.
        :param command: command to be processed.
        :return:None
        """
        command_params = command.split(" ")
        self.call(command_params,print_result)
