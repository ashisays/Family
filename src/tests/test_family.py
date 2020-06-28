from unittest import TestCase
from src.family import person
from src.family import family


class TestFamily(TestCase):
    def setUp(self):
        parent_male = person.Male("Rambo", None)
        parent_female = person.Female("Sydney", None)
        self.marriedFamilyMaleBloodline = family.Family(parent_male, parent=None, spouse=parent_female)
        self.singleFamily = family.Family(parent_male, parent=None)
        self.marriedFamilyFemaleBloodline = family.Family(parent_female, parent=None, spouse=parent_male)
        child_male = person.Male("Rambo Junior", None)
        child_female = person.Female("Sydney Junior", None)
        self.singleMale = family.Family(child_male, parent=None)
        self.singleFemale = family.Family(child_female, parent=None)

    def test_get_son_in_law_male_bloodline(self):
        if self.marriedFamilyMaleBloodline.get_son_in_law() is not None:
            self.fail("Got person %s for Male Bloodline" % self.marriedFamilyMaleBloodline.get_son_in_law())

    def test_get_daughter_in_law_male_bloodline(self):
        if self.marriedFamilyMaleBloodline.get_daughter_in_law() is None:
            self.fail("Got None for daughter in law in male Bloodline,which is not expected")

    def test_get_in_law_single_family(self):
        if self.singleFamily.get_son_in_law() is not None or self.singleFamily.get_daughter_in_law() is not None:
            self.fail("Got in laws info for single family which is not as expected.")

    def test_get_son_in_law_female_bloodline(self):
        if self.marriedFamilyFemaleBloodline.get_son_in_law() is None:
            self.fail("Got None for daughter in law in female Bloodline,which is not expected")

    def test_get_daughter_in_law_female_bloodline(self):
        if self.marriedFamilyFemaleBloodline.get_daughter_in_law() is not None:
            self.fail("Got daughter in law in female Bloodline,which is not expected")

    def test_add_children_to_single_family(self):
        if self.singleFamily.add_children(self.singleMale) is not False or \
                self.singleFamily.get_sons():
            self.fail("Got in sons info for single family,after adding which is not as expected.")

    def test_add_children_to_male_bloodline(self):
        if self.marriedFamilyMaleBloodline.add_children(self.singleMale) is False or \
                len(self.marriedFamilyMaleBloodline.get_sons()) is not 1:
            self.fail("Got in sons info ,after adding which is not as expected.")

    def test_add_children_to_female_bloodline(self):
        if self.marriedFamilyFemaleBloodline.add_children(self.singleMale) is False:
            self.fail("Unable to add children to the Female bloodline.")
        if len(self.marriedFamilyFemaleBloodline.get_sons()) is not 1:
            self.fail("Got incorrect sons info , expected 1 got %d."
                      %len(self.marriedFamilyFemaleBloodline.get_sons()))

    def test_add_multiple_time_same_children(self):
        # add child twice.
        self.marriedFamilyFemaleBloodline.add_children(self.singleFemale)
        self.marriedFamilyFemaleBloodline.add_children(self.singleFemale)
        if len(self.marriedFamilyFemaleBloodline.get_daughters()) is not 1:
            self.fail("Got %s daughter info for family,after adding twice which is not as expected."
                      % len(self.singleFamily.get_daughters()))
