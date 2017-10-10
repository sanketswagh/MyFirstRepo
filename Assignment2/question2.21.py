# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 18:45:31 2017

@author: Sanket Wagh
"""

try:    
     list = [12,24,35,24,88,120,155,88,120,155]
     print "Original List:- ",list
     myList = sorted(set(list))
     print "list after removing all duplicates:- ",myList
except Exception, e:
    print "Exception Handled Successfully : ", e