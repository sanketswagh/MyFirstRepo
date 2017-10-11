# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:33:06 2017

@author: Sanket Wagh
"""

class DemoClass:
    data = ""
    try:    
        def getData(self):
            print "Entered string is: ",data
                        
        def setData(self,data):
            DemoClass.data = data
                        
    except Exception, e:
        print "Exception Handled Successfully : ", e
d = DemoClass()
data = raw_input("Enter the string: ")
d.setData(data)
d.getData()