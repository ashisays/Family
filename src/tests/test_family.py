from unittest import TestCase
from src.family import person
from src.family import family
from src.family.constants import Message, Sex


class TestFamily(TestCase):
    def setUp(self):
        self.family = family.Family("Ashish", Sex.Male)
        self.family.add_spouse("Ashish", "Sonam", Sex.Female)
        self.family.add_child("Sonam","Raj", Sex.Male)
        self.family.add_spouse("Raj", "Preeti", Sex.Female)
        self.family.add_child("Sonam","Priya", Sex.Female)
        self.family.add_spouse("Priya", "Luv", Sex.Male)
        self.family.add_child("Priya", "kush", Sex.Male)
        self.family.add_child("Preeti", "Jay", Sex.Male)

    def test_search_family_member(self):
        if self.family.search_family_member(self.family.family_head, "Ashish") is None:
            self.fail("Unable to fund family heads.")

    def test_find_member_in_family_members(self):
        member_list = [self.family.family_head, self.family.family_head.get_spouse()]
        if self.family.find_member_in_family_members(member_list, "Sonam") is None:
            self.fail("Unable to find family spouse from list.")

    def test_add_spouse_negative(self):
        if self.family.add_spouse("Ashish", "Gusain", Sex.Female):
            self.fail("able to add  spouse to list,which is not expected.")

    def test_add_child_to_Male(self):
        if self.family.add_child("Ashish", "Ram", Sex.Female) != Message.CHILD_ADDITION_FAILED.value:
            self.fail("Able to add  child to list,which is not expected.")

    def test_add_child(self):
        if self.family.add_child("Sonam", "Ram", Sex.Female) != Message.CHILD_ADDITION_SUCCEEDED.value:
            self.fail("Not Able to add  child to list,which is not expected.")

    def test_add_child_and_get(self):
        child_before_addition = len(self.family.family_head.get_spouse().get_all_childs())
        self.family.add_child("Sonam", "Shyam", Sex.Female)
        child_after_addition = len(self.family.family_head.get_spouse().get_all_childs())
        if child_after_addition != (child_before_addition + 1):
            self.fail("Not Able to add  child to list,which is not expected.")

    def test_get_relationship(self):
        if self.family.get_relationship("Son","Lakshya") != Message.PERSON_NOT_FOUND.value:
            self.fail("Message is not as expected , PERSON_NOT_FOUND.")

    def test_get_childrens_from_family_single(self):
        jay = self.family.search_family_member(self.family.family_head,"Jay")
        if self.family.get_childrens_from_family(jay) != []:
            self.fail("Unable to find no children for single parent.")

    def test_search_family_member(self):
        ashish = self.family.search_family_member(self.family.family_head,"Ashish")
        if self.family.family_head != ashish:
            self.fail("family head object not match with searched object.")

    def test_find_member_in_family_members(self):
        ashish = self.family.search_family_member(self.family.family_head, "Ashish")
        jay = self.family.search_family_member(self.family.family_head, "Jay")
        searched_member = self.family.find_member_in_family_members([ashish,jay],"Jay")
        if searched_member != jay:
            self.fail("family head object not match with searched object.")

    def test_search_siblings(self):
        siblings = self.family.search_siblings("Raj")
        if siblings[0] != "Priya":
            self.fail("Value is not as expected.")

    def test_search_son(self):
        siblings = self.family.search_son("Raj")
        if siblings[0] != "Jay":
            self.fail("Value is not as expected.")

    def test_search_daughters(self):
        siblings = self.family.search_daughters("Ashish")
        if siblings[0] != "Priya":
            self.fail("Value is not as expected.")

    def test_search_brother_in_law(self):
        brother_in_law = self.family.search_brother_in_law("Luv")
        if brother_in_law[0] != "Raj":
            self.fail("Value is not as expected.")

    def test_search_sister_in_law(self):
        sister_in_law = self.family.search_sister_in_law("Preeti")
        if sister_in_law[0] != "Priya":
            self.fail("Value is not as expected.")

    def test_search_maternal_aunt(self):
        maternal_aunt = self.family.search_maternal_aunt("kush")
        if maternal_aunt:
            self.fail("Value is not as expected.")

    def test_search_maternal_uncle(self):
        maternal_uncle = self.family.search_maternal_uncle("kush")
        if maternal_uncle[0]!="Raj":
            self.fail("Value is not as expected.")

    def test_search_paternal_aunt(self):
        paternal_aunt = self.family.search_paternal_aunt("Jay")
        if paternal_aunt[0]!="Priya":
            self.fail("Value is not as expected.")

    def test_search_paternal_uncle(self):
        paternal_uncle = self.family.search_paternal_uncle("Jay")
        if paternal_uncle:
            self.fail("Value is not as expected.")
