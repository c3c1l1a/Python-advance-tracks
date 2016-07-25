from runner.koan import *
from koan_labs.prime_factors import *
class AboutPrimeFactors(Koan):
	def test_about_prime_factors(self):
		"""
		This is yet another exercise that helps you understand how looping and integer operators work.

	 	ACTIVITY
	 	========

		Go to koan_labs/about_prime_factors.py and edit the function largest_prime_factor(). The function is supposed to
		take a number as an argument and return the largest prime factor of the provided number.
		For example, the prime factors of 13195 are 5, 7, 13 and 29. The function should 
		return 29 as the largest prime factor.
		"""
		self.assertEqual(largest_prime_factor(600851), 20719, "Given 600851, the largest prime factor is 20719")
		self.assertEqual(largest_prime_factor(7477484), 683, "Given 7477484, the largest prime factor is 683")
		self.assertEqual(largest_prime_factor(6477338), 462667, "Given 6477338, the largest prime factor is 462667")
		self.assertEqual(largest_prime_factor(5253), 103, "Given 5253, the largest prime factor is 103")
		self.assertEqual(largest_prime_factor(8927), 113, "Given 8927, the largest prime factor is 113")
		
		
