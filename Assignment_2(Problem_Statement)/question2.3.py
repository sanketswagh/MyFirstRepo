# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:20:59 2017

@author: Sanket Wagh
"""
 
for row in range(0,5):    
    for column in range(0,row+1):
        print "*",
    print "\n"
 
for row in range(6, 10):    
    for column in range(10, row, -1):
        print "*",
    print "\n"