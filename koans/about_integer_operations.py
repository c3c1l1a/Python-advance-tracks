from runner.koan import *
from koan_labs.integer_operations import * 

class AboutIntegerOperations(Koan):
	def test_integer_addition(self):
		"""
		This activity question will help you understand how looping and integer operations work.

		ACTIVITY
		========
		Open koan_labs/integer_operations.py. Inside the integer_operations function, write code that takes an initial 
		value which can be any random integer between 0 and 2 billion, prints out the next 5 numbers after the initial one, 
		calculates the sum(including the initial number) and returns it.
		"""
		self.assertEqual(integer_operations(45), 285,"For an intial value of 45, the expected sum was 285")
		self.assertEqual(integer_operations(56), 351,"For an intial value of 56, the expected sum was 351")
		self.assertEqual(integer_operations(13), 93,"For an intial value of 13, the expected sum was 93")
		self.assertEqual(integer_operations(45723833282), 274342999707 ,"For an intial value of 45723833282 , the expected sum was 274342999707 ")
		self.assertEqual(integer_operations(136378283), 818269713 ,"For an intial value of 136378283, the expected sum was 818269713")





