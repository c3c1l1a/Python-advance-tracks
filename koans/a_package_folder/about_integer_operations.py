from runner.koan import *
from koan_labs.integer_operations import * 

class AboutIntegerOperations(Koan):
	def test_integer_addition(self):
		"""
		This is yet another question thst will help you understand how looping and integer opearations work.

		ACTIVITY 1
		===========
		Open koan_labs/integer_operations.py. Inside the integer_operations function, write code that prompts
		the user for a random integer between 0 and 2 billion, prints out the next 5 numbers after the entered number 
		and calculates the sum.
		Hints: You can create an initiale variabl that takes in the random number, a variable named total 
			initialized to zero, then loop 5 times updating the initial variable as you also update the sum.

		"""
		self.assertEqual(integer_operations(45), 285,"The expected sum was 285")
		self.assertEqual(integer_operations(56), 351,"The expected sum was 351")
		self.assertEqual(integer_operations(13), 93,"The expected sum was 93")
		self.assertEqual(integer_operations(45723833282), 274342999707 ,"The expected sum was 274342999707 ")
		self.assertEqual(integer_operations(136378283), 818269713 ,"The expected sum was 818269713")





