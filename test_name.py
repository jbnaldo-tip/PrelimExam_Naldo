import unittest

def name(x):

    return x == 'MIGUEL'

class myTest(unittest.TestCase):

    def test(self):

        self.assertTrue(name('MIGUEL'))

if __name__ == '__main__':

    unittest.main()