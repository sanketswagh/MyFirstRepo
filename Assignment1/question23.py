# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:24:10 2017

@author: Sanket Wagh
"""
import logging
string = raw_input("Enter the string: ")
file0 = open('abc.txt','a+')
file0.write(string)
logging.warning('Entry made into file....!!!')
file1 = open('abc.txt','r')


list1 = []
print "Contents of Modified File:\n",
for i in file1:
    list1.append(i)
print list1
    