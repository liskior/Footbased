import unittest
from time import sleep
from mapping import Mapping

DELAY = 0.4
m = None

class MyUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global m
        m = Mapping()
        sleep(2)

class MyFirstSetOfTests(MyUnitTest):

    def test1(self):
        sleep(DELAY)
        global m
        m.show(1)
        print('m.show(0)')
        sleep(DELAY)
        m.click(2, 1)
        sleep(10)

#    def test2(self):
#        sleep(DELAY)
#        self.m.click(1, 1)
#        sleep(DELAY)
#        self.m.click(1, 2)
#
#        # Du kannst auch:
#        actual = True
#        expected = True
#        self.assertEqual(actual, expected)
#        # Aber egal, weil "nicht crashen" reicht.


if __name__ == '__main__':
    unittest.main()
