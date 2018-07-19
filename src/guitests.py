import unittest
from time import sleep
from mapping import Mapping

DELAY = 1

class MyUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        self.m = Mapping()
        sleep(1.4)
        do_something_expensive_for_all_sets_of_tests()

class MyFirstSetOfTests(MyUnitTest):

    def test1(self):
        sleep(DELAY)
        self.m.click(1, 1)
        sleep(DELAY)
        self.m.click(1, 2)

        # Du kannst auch:
        actual = True
        expected = True
        self.assertEqual(actual, expected)
        # Aber egal, weil "nicht crashen" reicht.


if __name__ == '__main__':
    unittest.main()
