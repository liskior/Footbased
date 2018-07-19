import unittest
from time import sleep
from mapping import Mapping

DELAY = 1
m = None

class MyUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global m
        m = Mapping()
        sleep(10)

class MyFirstSetOfTests(MyUnitTest):

    def test1(self):
        sleep(DELAY)
        global m
        m.show(0)
        print 'm.show(0)'
        sleep(DELAY)
        #m.click(1, 0)

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
