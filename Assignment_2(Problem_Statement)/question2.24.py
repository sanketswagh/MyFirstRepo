# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:22:02 2017

@author: Sanket Wagh
"""
import re
try:
    seq = raw_input("Enter the sequence: ") 
    print re.findall("\d+",seq)
except Exception:
    print "Exception Handled Successfully"