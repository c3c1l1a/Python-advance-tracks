#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The path to enlightenment starts with the following:

import unittest

from koans.about_how_the_lesson_works import AboutHowTheTrackWorks
from koans.about_expressions_and_statements import AboutExpressionsAndStatements


def koans():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None
    suite.addTests(loader.loadTestsFromTestCase(AboutHowTheTrackWorks))
    suite.addTests(loader.loadTestsFromTestCase(AboutExpressionsAndStatements))

    return suite
