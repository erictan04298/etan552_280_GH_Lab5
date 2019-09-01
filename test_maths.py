import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    def test_factorial(self):
        result = maths.factorial(3)
        self.assertEqual(result, 6, "failed")
        


# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
