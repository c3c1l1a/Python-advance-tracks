from runner.koan import *
from koan_labs.multiples import*

class AboutMultiples(Koan):
	def test_about_how_multiples_work(self):
		"""
	 	This is yet another exercise that helps you understand how looping and integer operators work.

	 	ACTIVITY
	 	========
	 	In the file koan_labs/multiples.py, edit the function to return the sum of all multiples of 
	 	3 and 5 below 1000.
	 	Hint:
	 	list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
		Find the sum of all the multiples of 3 or 5 below 1000
		"""
		self.assertEqual(multiple_sum(), 233168, "The expected answer was 233168")
