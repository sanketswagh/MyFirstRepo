# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:51:01 2017

@author: Sanket Wagh
"""

import math

list1=[12,24,35,70,88,120,155]
try:
    def binarySearch(list, element):
        low = 0
        high = len(list)-1
        index = -1
        while high>=low and index==-1:
            mid = int(math.floor((high+low)/2.0))
            if list[mid]==element:
                index = mid
            elif list[mid]>element:
                high = mid-1
            else:
                low = mid+1
        return index
except Exception:
    print "Exception Handled Successfully"
    
print "Index of Element 155 is: ",binarySearch(list1,155)