# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 12:09:19 2017

@author: Sanket Wagh
"""
try:
    num = int(input("Enter the number: "))
    sum = 0
    while(num > 0):
        digit = num % 10
        sum = sum + digit
        num = num / 10
    print ("Sum of digits in the number : ",sum)
except Exception:
    print "Exception Handled Successfully"