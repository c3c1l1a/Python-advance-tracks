from runner.koan import *
from koan_labs.strings_count import * 
class AboutStringsCount(koans):
	def test_string_count(self):
		"""
		This is yet another question that will help get a deeper understanding of strings and looping.

		ACTIVITY 1
		===========
		Go to koan_labs/strings_count.py. In function count_letter_b, add code that  takes in a string as input,
		counts the frequency of the letter 'b' irrespective of the case. Return the number of instances of B's in the string.
		"""

		self.assertEqual(count_letter_b(“Bcdgdhhhskkbjohhudbh74Y38BEFNFRIJbBmjdnfjhbbBhhkdiuBduhbbhuhbhskjsbhbbjbhbgrubhhuhivuhhbbuhebbebbbBbbbTghFGDGGSJbB”), 32, "The expected frequency is 32"))
		self.assertEqual(count_letter_b("ggrrgrejhrhrtrjccvbbyGGHBBGNHFYYGHHTFKJVHgH"), 4 , The expected count was 4)
		self.assertEqual(count_letter_b("jdhugdgdvgdshvdshsgdsudvjbgvvxssjhkvshdudjhsjgc cshsvvzcdh"), 1 , The expected count was 1)
		self.assertEqual(count_letter_b("boy"), 1, The expected count was 1)