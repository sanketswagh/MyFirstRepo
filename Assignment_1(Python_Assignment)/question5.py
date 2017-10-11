# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 12:23:38 2017

@author: Sanket Wagh
"""

try:
    def getMissingNo(A):
        n = len(A)
        total = (n+1)*(n+2)/2
        sum_of_A = sum(A)
        return total - sum_of_A
    A = [1, 2, 4, 5, 6]
    miss = getMissingNo(A)
    print(miss)
except Exception, e:
    print "Exception Handled Successfully : ", e