from unittest import TestCase
from src.family import person

class TestPerson(TestCase):
    def setUp(self):
        self.boy = person.Male("a", None)
        self.girl = person.Female("a", None)

    def test_is_boy(self):
        if not self.boy.is_boy():
            self.fail("Testcase failed , exected True found %s" % self.boy.is_boy())

    def test_is_girl(self):
        if not self.girl.is_girl():
            self.fail("Testcase failed , exected True found %s" % self.girl.is_girl())
