from unittest import TestCase
from src.family import person
from src.family import family
from src.family.constants import Message


class TestFamily(TestCase):
    def setUp(self):
        self.family = family.Family("Ashish", "Male")
        self.family.add_spouse("Ashish", "Sonam", "Female")

    def test_search_family_member(self):
        if self.family.search_family_member(self.family.family_head, "Ashish") is None:
            self.fail("Unable to fund family heads.")

    def test_find_member_in_family_members(self):
        member_list = [self.family.family_head, self.family.family_head.get_spouse()]
        if self.family.find_member_in_family_members(member_list, "Sonam") is None:
            self.fail("Unable to find family spouse from list.")

    def test_add_spouse_negative(self):
        if self.family.add_spouse("Ashish", "Gusain", "female"):
            self.fail("able to add  spouse to list,which is not expected.")

    def test_add_child_to_Male(self):
        if self.family.add_child("Ashish", "Ram", "female") != Message.CHILD_ADDITION_FAILED:
            self.fail("Able to add  child to list,which is not expected.")

    def test_add_child(self):
        if self.family.add_child("Sonam", "Ram", "female") != Message.CHILD_ADDITION_SUCCEEDED:
            self.fail("Not Able to add  child to list,which is not expected.")

    def test_add_child_and_get(self):
        child_before_addition = len(self.family.family_head.get_spouse().get_all_childs())
        self.family.add_child("Sonam", "Shyam", "female")
        child_after_addition = len(self.family.family_head.get_spouse().get_all_childs())
        if child_after_addition != (child_before_addition + 1):
            self.fail("Not Able to add  child to list,which is not expected.")
