#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
from koan_labs.how_the_track_works import * 



class AboutHowTheTrackWorks(Koan):

    def test_demo_acitivity1(self):
        """
        Prerequisites: https://www.codecademy.com/learn/python

        Hello and welcome to the python advance track Section 1. This section requires that you have some background in python. 
        If you don't have any python background, then the codecademy python track will get you upto speed and help you make 
        the most out of this track.  The section is structured around activities and challenges. We like using the agile 
        developement methodology and TDD is at the heart of it. That said, the challenges and activities will be a set of test 
        suites that require you to write some code to make the tests pass.

        Every challenge/activity will have some instructions in RED just like this one, elaborating what the challenge is 
        about and at times links to useful resources will be provided to help you find solutions.
        
        Let's do one simple example activity to demonstrate what the above means.

        DEMO ACTIVITY 1
        ===============

        Instructions for the demo activity
        ===================================
        Open the file koan_labs/how_the_track_works.py. Make demo_activity1 function return True. 

        """
        self.assertTrue(demo_activity1(), "demo_activity function did not return True")

    def test_demo_activity2(self):
        """
        
        Nice work. Hope that wasn't too hard. 

        Let us try another demo activity, just to make sure you understand how this works.

        DEMO ACTIVITY 2
        ===============

        Instructions for the demo activity 2
        ====================================
        Open koan_labs/how_the_track_works.py. Create a function called demo_acitivity2. The function should return 
        the value 2

        """
        self.assertEqual(demo_activity2(), 2, "demo_activity2 function did not return 2")

   
 