import unittest
from calculator import *  

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc1 = Calculator(CalcImplementation())  
        #self.calc1 = Calculator(BuggyCalcImplementation())  

    def test_add(self):
        self.assertEqual(self.calc1.add(2, 0), 2)
        self.assertEqual(self.calc1.add(2, 3), 5)
        self.assertEqual(self.calc1.add(-1, 1), 0)
        self.assertEqual(self.calc1.add(-5, 0), -5)
        self.assertEqual(self.calc1.add(-5, -1), -6)

    def test_subtract(self):
        self.assertEqual(self.calc1.subtract(5, 0), 5)
        self.assertEqual(self.calc1.subtract(5, 3), 2)
        self.assertEqual(self.calc1.subtract(1, 1), 0)
        self.assertEqual(self.calc1.subtract(-5, -3), -2)
        self.assertEqual(self.calc1.subtract(-1, 2), -3)

    def test_multiply(self):
        self.assertEqual(self.calc1.multiply(2, 1), 2)
        self.assertEqual(self.calc1.multiply(2, 2), 4)
        self.assertEqual(self.calc1.multiply(2, 3), 6)
        self.assertEqual(self.calc1.multiply(-2, 3), -6)
        self.assertEqual(self.calc1.multiply(2, -3), -6)
        self.assertEqual(self.calc1.multiply(-1, -3), 3)

    def test_divide(self):
        self.assertEqual(self.calc1.divide(2, 1), 2)
        self.assertEqual(self.calc1.divide(2, -1), -2)
        self.assertEqual(self.calc1.divide(1, 2), 1/2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
