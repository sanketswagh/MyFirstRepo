# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 10:48:01 2017

@author: Sanket Wagh
"""
k=65
try:
    for i in range(6):
        for j in range(1, i+1):
            a = chr(k)
            print a,
            k=k+1
        print
except Exception:
    print "Exception Handled Successfully"