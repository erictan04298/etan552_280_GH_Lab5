import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        result = maths.add(2, 6, 2)
        self.assertEqual(result, "1000", "")

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        result =  maths.fibonacci(5)
        self.assertEqual(result, 8, "")
    '''
    def test_convert_base(self):
        result = maths.convert_base(8, 2)
        self.assertEqual(result,"1000", "")
        '''
    def test_factorial(self):
        result = maths.factorial(3)
        self.assertEqual(result, 6, "failed")
        


# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
