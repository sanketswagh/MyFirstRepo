# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:52:55 2017

@author: Sanket Wagh
"""

num=int(raw_input("Enter the number: "))
if (num > 1):
    d=dict()
    for i in range(1,num+1):
        d[i]=i*i
    
    print d
else:
    print "Kindly enter a Integral Number....!!!"