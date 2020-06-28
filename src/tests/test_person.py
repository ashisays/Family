from unittest import TestCase
from src.family import person

class TestPerson(TestCase):
    def setUp(self):
        self.boy = person.Male("a", None)
        self.girl = person.Female("a", None)

    def test_is_boy(self):
        if not self.boy.isBoy():
            self.fail("Testcase failed , exected True found %s" %self.boy.isBoy())

    def test_is_girl(self):
        if not self.girl.isGirl():
            self.fail("Testcase failed , exected True found %s" % self.girl.isGirl())
