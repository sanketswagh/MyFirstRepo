# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:17:22 2017

@author: Sanket Wagh
"""

def fun(num):
        return num > 0 and (num & (num - 1)) == 0

num1 = int(raw_input("Enter the number to check: "))
print("The is a power of 2: ",fun(num1))
