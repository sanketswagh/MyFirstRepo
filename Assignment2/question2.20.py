# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:53:07 2017

@author: Sanket Wagh
"""

class Person:
    try:    
       def getGender(self):
          print "Parent"
          return
    except Exception, e:
        print "Exception Handled Successfully : ", e
class Male(Person):
    try:    
       def getGender(self):
          print 'Male'
          return
    except Exception, e:
        print "Exception Handled Successfully : ", e
class Female(Person):
    try:    
       def getGender(self):
          print "Female"
          return
    except Exception, e:
        print "Exception Handled Successfully : ", e
p = Person()
m = Male()
f = Female()
p.getGender(),
m.getGender(),
f.getGender(),