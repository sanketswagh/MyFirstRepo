# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 18:01:23 2017

@author: Sanket Wagh
"""
try:
    lst=[]
    for i in range(1500, 2700):
        if (i%7==0) and (i%5==0):
            lst.append(str(i))
    print (','.join(lst))
except Exception, e:
        print "Exception Handled Successfully : ", e   