# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:25:03 2017

@author: Sanket Wagh
"""

num = int(raw_input("Enter the number: "))

if (num > 0):
#    while (num != 1):
        print "The sequence is: ",num,
        while num != 1:
            if (num%2 == 0):
                num = num / 2
            else:
                num = num * 3 + 1
            print num,
else: 
    print "Enter a positive integer to continue!!!"
