"""
test program
@author: jm
"""
import unittest

class TestHello(unittest.TestCase):
    def testHello(self): 
        self.assertEqual(1+1,2)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()