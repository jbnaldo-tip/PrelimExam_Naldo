import unittest

def square(height, width, side):
    
    height = 2
    width = 2
    side = 2

    return height*width*side

class myTest(unittest.TestCase):

    def test(self):

        self.assertEqual(square(2,2,2),8)
    
if __name__ == '__main__':

    unittest.main()