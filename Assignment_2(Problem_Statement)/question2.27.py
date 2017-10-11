# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:13:16 2017

@author: Sanket Wagh
"""

tuple1 = (1,2,3,4,5,6,7,8,9,10)
list1 = list()
for i in range(len(tuple1)):
    if (tuple1[i]%2==0):
        list1.append(tuple1[i])
tuple2=tuple(list1)
print tuple2
        