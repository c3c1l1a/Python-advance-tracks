from runner.koan import *
from koan_labs.prime_factors import *
class AboutPrimeFactors(koans):
	def about_prime_factors(self):
		"""
		Go to koan_labs/about_prime_factors.py and edit the function largest_prime_factor().
		The function is supposed to return the largest prime factor of the provide number.
		For example, the prime factors of 13195 are 5, 7, 13 and 29. The function should 
		return 29 as the largest prime factor.
		"""
		self.assertEqual(argest_prime_factor(600851475143), 20719, "The expected result was 201719")
		self.assertEqual(argest_prime_factor(7477484), 683, "The expected result was 683")
		self.assertEqual(argest_prime_factor(6477338), 462667, "The expected result was 462667")
		self.assertEqual(argest_prime_factor(5253), 103, "The expected result was 103")
		self.assertEqual(argest_prime_factor(8927), 113, "The expected result was 113")
		
		
