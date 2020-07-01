from unittest import TestCase

from src.family.constants import Sex, Message
from src.familyapi import FamilyAPI


class TestFamilyAPI(TestCase):
    def setUp(self):
        self.api = FamilyAPI()
        self.api.add_family_head("Ashish",Sex.Male)

    def test_call(self):
        if self.api.call("xyz") != Message.INVALID_COMMAND.value:
            self.fail("Api call failed")

    def test_invalid_cmd(self):
        if self.api.invalid_cmd() != Message.INVALID_COMMAND.value:
            self.fail("invalid cmd failed")

    def test_add_child(self):
        if self.api.add_child("Ashish", "Ram", "Female") != Message.CHILD_ADDITION_FAILED.value:
            self.fail("Child addition failed")

    def test_add_spouse(self):
        if self.api.add_spouse("Ashish", "Ram", "Female") is not None:
            self.fail("Child addition failed")

    def test_get_relationship(self):
        if self.api.get_relationship("Ashish", "Son") != Message.NONE.value:
            self.fail("Child addition failed")

    def test_process_input_command(self):
        if self.api.process_input_command("xyz ABC ASD ASD") != None:
            self.fail("Api call failed")

