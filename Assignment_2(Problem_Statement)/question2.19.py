# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:42:45 2017

@author: Sanket Wagh
"""
dict = {}
string=raw_input("Enter the string: ")
for i in string:
    dict[i] = dict.get(i,0)+1
print '\n'.join(['%s,%s' % (a, b) for a, b in dict.items()])