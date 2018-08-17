""" Unit tests for the GUI.

At some point it got frustrating, trying out the GUI manually each time. So we
implemented this.

This script is of no significance to the core machine learning functionality.

"""

import unittest
from time import sleep
from mapping import Mapping

DELAY = 0.4
DELAY = 1
m = None

def run(cmd):
    global m
    print('Executing ' + cmd)
    eval(cmd)
    sleep(DELAY)

class MyUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global m
        m = Mapping()
        sleep(2)


class MyFirstSetOfTests(MyUnitTest):

    @unittest.skip('skipthis')
    def test1(self):
        global m
        m.show(1)
        m.click(2, 1)
        print 'SUCCESS'

    @unittest.skip('skipthis')
    def test2(self):
        sleep(DELAY)
        global m
        run('m.open_list(2)')
        run('m.open_list(2)')
        run('m.open_list(1)')
        run('m.open_list(0)')

    @unittest.skip('skipthis')
    def test3(self):
        sleep(DELAY)
        global m
        run('m.open_list(0)')
        run('m.choose(0)')
        run('m.choose(1)')
        run('m.choose(2)')
        run('m.choose(3)')
        run('m.choose(4)')
        run('m.choose(3)')
        run('m.choose(2)')
        run('m.choose(1)')
        run('m.choose(0)')

    def test4(self):
        sleep(DELAY)
        global m
        run('m.click(2,0)')

        run('m.click(1,0)')
        run('m.click(1,1)')
        run('m.click(1,2)')

        run('m.click(2,0)')

        run('m.click(0,0)')
        run('m.click(0,1)')
        run('m.click(0,2)')
        run('m.click(0,3)')
        run('m.click(0,4)')
        run('m.click(0,3)')
        run('m.click(0,2)')
        run('m.click(0,1)')
        run('m.click(0,0)')

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
    print('DONT WORRY ABOUT THE LAST ERROR IF YOU SEE OK.')
    unittest.main()
