# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:48:32 2017

@author: Sanket Wagh
"""

num = int(raw_input("Input a dog's age in human years: "))
for i in range(1,num-1):
    result = i*4
result = result + 21
print "The dog's age in dog's years is",result