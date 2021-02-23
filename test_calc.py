import calculator
import unittest

class TestCalc(unittest.TestCase):

	def test_add(self):
		result=calculator.add(10,5)
		self.assertEqual(result,15)
	def test_sub(self):
		result=calculator.sub(10,5)
		self.assertEqual(result,5)
	def test_mul(self):
		result=calculator.mul(10,5)
		self.assertEqual(result,50)
	def test_div(self):
		result=calculator.div(10,5)
		self.assertEqual(result,2)

	


if __name__=='__main__':
        unittest.main()
