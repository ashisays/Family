from unittest import TestCase

from src import familyapi


class Test(TestCase):
    def test_create_family_tree(self):
        tree = familyapi.create_family_tree("Ashish", "Sonam")
        if "Ashish" not in tree.familyMembers:
            self.fail("family tree did not have expected value Ashish")

    def test_add_descendants(self):
        tree = familyapi.create_family_tree("Ashish", "Sonam")
        familyapi.add_descendants(tree, "Ashish", "Ram", "male")
        if "Ram" not in tree.familyMembers:
            self.fail("family tree did not have expected value Ram")
