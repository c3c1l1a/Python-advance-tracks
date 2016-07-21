#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
#import mock
from koan_labs.expressions_and_statements import * 



class AboutExpressionsAndStatements(Koan):

    def test_compounded_principal(self):
    	"""
    		This is yet another series of activities that will help you understand about how expressions and statements work.

    		ACTIVITY 1
    		===========
    		Open koan_labs/expressions_and_statements.py. Inside the compounded_principle function, create a variable P and 
    		assign it the principal amount of 10000. Create another variable n and assign it the value 1, and finally assign
    		to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money 
    		will be compounded for. Calculate and print the final amount after t years. Return the amount. The formular for calculating
    		compunded intererest is 

    			A = P (1 + (r/n)) ^ nt

    			Where:
    			P = Principal amount
    			r = annual nominal interest rate
    			n = number of times the interest in compunded per year
    			t = number of years
                """
    	#with mock.patch('__builtin__.raw_input', side_effect=[30, 10, 40, 1.5, 3, 1, 8.1]):
        self.assertEqual(compounded_principal(30), 100626, "The correct amount after 10 years should be 10626" )
        self.assertEqual(compounded_principal(10), 21589, "The correct amount after 10 years should be 21589"  )
    	self.assertEqual(compounded_principal(40), 217245, "The correct amount after 40 years should be 217245")
    	self.assertEqual(compounded_principal(1.5), 11223, "The correct amount after 1.5 years should be 11223" )
        self.assertEqual(compounded_principal(3), 12597, "The correct amount after 3 years should be 12597")    		
        self.assertEqual(compounded_principal(1), 10800 , "The correct amount after 1 year should be 10800" )
        self.assertEqual(compounded_principal(8.1), 18652, "The correct amount after 8.1 years should be 18652" )