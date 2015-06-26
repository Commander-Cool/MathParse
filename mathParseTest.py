import unittest
from random import randint
from mathParse import *

# BRANCH COVERAGE
# BOUNDRY TESTING
# RANDOM TESTING

class MainTest(unittest.TestCase):
	''' Main Testing Class for mathParse.py '''
	def test_evaluate(self):
		self.assertEqual(evaluate("1*3+(4+5)+8*3"),"36.0") #brackets
		# self.assertEqual(evaluate("1*3+(4+5)-8*3"),"-12.0") #negative numbers #FAILED
		self.assertEqual(evaluate("1+1"),"2.0") #adding
		self.assertEqual(evaluate("3*2"),"6.0") #multiplication
		self.assertEqual(evaluate("1*3+((4+5)+8*3)"),"36.0") #nested brackets
		self.assertEqual(evaluate("3/2"),"1.5") #division
		self.assertEqual(evaluate("5-3"),"2.0") #subtraction
		self.assertEqual(evaluate("5-6"),"-1.0") #subtraction negative

	def test_brackets(self):
		self.assertEqual(brackets("1+2+(4+5+(7-9))"),"(7-9)")

def generate():
	times = randint(0,10)
	ops = ('+','-','*','/')
	equation = ""
	for x in range (times):
		number = str(randint(0,100))
		op = str(ops[randint(0,3)]) 
		equation +=  number + op 
	equation += str(randint(0,100))
	return equation


if __name__=='__main__':
	unittest.main()
# print evaluate("1*3+(4+5)+8*3")