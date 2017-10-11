# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:02:34 2017

@author: Sanket Wagh
"""
try:
    alpha = raw_input("Input a letter of the alphabet: ")
    
    if alpha in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
    	print("%s is a vowel." % alpha)
    else:
    	print("%s is a consonant." % alpha) 
except Exception:
    print "Exception Handled Successfully"     