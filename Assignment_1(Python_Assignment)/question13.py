# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:25:03 2017

@author: Sanket Wagh
"""

num = int(raw_input("Enter the number: "))
result = [] 
if (num > 0):
#    while (result == 1):
        if (num%2 == 0):
            result.append(num/2)
            print result
        else:
            result.append((num*3)+1)
            print result
else: 
    print "Enter a positive integer to continue"
