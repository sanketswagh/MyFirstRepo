# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:09:37 2017

@author: Sanket Wagh
"""

file1 = open('abc.txt','r')
list1 = []
print "Contents of File:\n",
for i in file1:
    list1.append(i)
print list1
print "***********************************************************************\n"
print "Contents of File in Reverse Order: "
for j in reversed(list1):  
    print j
#print "Number of lines: ",lines