#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The path to enlightenment starts with the following:

import unittest

from koans.about_how_the_lesson_works import AboutHowTheTrackWorks
from koans.about_expressions_and_statements import AboutExpressionsAndStatements
from koans.about_integer_operations import AboutIntegerOperations
from koans.about_multiples import AboutMultiples
from koans.about_prime_factor import AboutPrimeFactors
from koans.about_strings_count import AboutStringsCount

def koans():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None
    #suite.addTests(loader.loadTestsFromTestCase(AboutHowTheTrackWorks))
    #suite.addTests(loader.loadTestsFromTestCase(AboutIntegerOperations))
    #suite.addTests(loader.loadTestsFromTestCase(AboutMultiples))
    #suite.addTests(loader.loadTestsFromTestCase(AboutPrimeFactors))
    #suite.addTests(loader.loadTestsFromTestCase(AboutExpressionsAndStatements))
    suite.addTests(loader.loadTestsFromTestCase(AboutStringsCount))

    return suite
