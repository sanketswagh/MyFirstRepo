# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:56:39 2017

@author: Sanket Wagh
"""
#filename = "C:\Program Files\Git\MyFirstRepo\Assignment1\abc.txt"
file1 = open('abc.txt','r')
lines = 0
for i in file1:
    lines += 1
print "Number of lines: ",lines