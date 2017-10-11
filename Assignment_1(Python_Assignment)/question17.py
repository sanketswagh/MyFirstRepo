# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:30:32 2017

@author: Sanket Wagh
"""
radius = 0
pi = 3.14
class Circle:
    try:    
        def computeArea(self,radius):
               area = pi * radius * radius
               print "Area is: ",area
    except Exception, e:
        print "Exception Handled Successfully : ", e
c = Circle()
radius = int(raw_input("Enter the radius: "))
c.computeArea(radius)