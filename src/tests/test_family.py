from unittest import TestCase
from src.family import person
from src.family import family


class TestFamily(TestCase):
    def setUp(self):
        self.family = family.Family("Ashish","male")
        self.family.add_spouse("Ashish","Sonam","female")

    def test_search_family_member(self):
        if self.family.search_family_member(self.family.family_head,"Ashish") is None:
            self.fail("Unable to fund family heads.")

    def test_find_member_in_family_members(self):
        member_list = [self.family.family_head,self.family.family_head.get_spouse()]
        if self.family.find_member_in_family_members(member_list,"Sonam") is None:
            self.fail("Unable to find family spouse from list.")

    def test_add_spouse_negative(self):
        if self.family.add_spouse("Ashish","Gusain","female"):
            self.fail("able to add  spouse to list,which is not expected.")
