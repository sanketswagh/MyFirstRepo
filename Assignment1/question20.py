# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:07:57 2017

@author: Sanket Wagh
"""
dict0 = {}
seq=raw_input("Enter the sequence: ")
list1=seq.split()

for i in list1:
    dict0[i] = dict0.get(i,0)+1

i = dict0.keys()
i.sort()

for words in i:
    print ("%s:%d" % (words,dict0[words]))