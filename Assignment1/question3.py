# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 11:53:18 2017

@author: Sanket Wagh
"""
def takelast(elem):
    return elem[2]
try:
    list1 = [(7,1,6),(3,4,9),(5,6,4),(4,7,1)]
    sortedList = sorted(list1,key=takelast)
    print ("Sorted List: ",sortedList)
except Exception:
    print "Exception Handled Successfully"