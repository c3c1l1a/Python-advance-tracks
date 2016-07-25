#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Acknowledgment:
#
# Python Koans Advance track is a port of Python Koans. There are some difference and tweeks added to
# cater for more questions and edge cases, but a great deal of it has been copied wholesale.
# So thank guys and have a nice time learning
#

import sys


if __name__ == '__main__':
    if sys.version_info >= (3, 0):
        print("\nThis is the Python 2 version of Python Koans, but you are " +
              "running it with Python 3 or newer!\n\n"
              "Did you accidentally use the wrong python script? \nTry:\n\n" +
              "    python contemplate_koans.py\n")
    else:
        if sys.version_info < (2, 7):
            print("\n" +
                  "********************************************************\n" +
                  "WARNING:\n" +
                  "This version of Python Koans was designed for " +
                  "Python 2.7 or greater.\n" +
                  "Your version of Python is older, so you may run into " +
                  "problems!\n\n" +
                  "But lets see how far we get...\n" +
                  "********************************************************\n")

        from runner.mountain import Mountain
        
        Mountain().walk_the_path(sys.argv)
