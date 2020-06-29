from unittest import TestCase
from src.family import person
from src.family.constants import Sex


class TestPerson(TestCase):
    def setUp(self):
        self.mother = person.Female("Kaikai")
        self.father = person.Male("Dasrath")
        self.boy = person.Male("Ram", mother=self.mother, father=self.father)
        self.girl = person.Female("Sita", None)

    def test_is_boy(self):
        if not self.boy.is_boy():
            self.fail("Testcase failed , exected True found %s" % self.boy.is_boy())

    def test_is_girl(self):
        if not self.girl.is_girl():
            self.fail("Testcase failed , exected True found %s" % self.girl.is_girl())

    def test_get_sex(self):
        if self.girl.get_sex() != Sex.female:
            self.fail("Testcase failed , exected female found Male")

    def test_get_parent_name(self):
        father_name, mother_name = self.boy.get_parent_name()
        if (father_name, mother_name) != (self.father.name, self.mother.name):
            self.fail("parent name is not correct,expected [%s,%s] , found [%s,%s]"
                      % (self.father.name, self.mother.name, father_name, mother_name))

    def test_get_mother(self):
        if self.boy.get_mother() != self.mother:
            self.fail("Mother is not found as expected.")


    def test_get_father(self):
        if self.boy.get_father() != self.father:
            self.fail("Father is not found as expected.")

    def test_add_none_spouse(self):
        if self.boy.add_spouse(self.boy):
            self.fail("Same sex spouse added which is not expected.")

    def test_add_and_get_spouse(self):
        fail = 0
        if not self.boy.add_spouse(self.girl):
            fail += 1
            print("Addition of spouse Failed.")
        if self.boy.get_spouse() is None:
            fail += 1
            print("Spouse for boy is come as None")
        if self.girl.get_spouse() is None:
            fail += 1
            print("Spouse for Girl has come as None")
        if fail:
            self.fail("Addition and fetching of spouse failed, check above for issue.")
