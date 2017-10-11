# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:47:04 2017

@author: Sanket Wagh
"""

class ListDemo:
    list1 = []
    try:    
        def getList(self):
            print "List is: ",list1
                        
        def setList(self,list1):
            ListDemo.list1.append(list1)
        
        def removeList(self,element):
            del list1[element]
            l.getList()
                        
    except Exception, e:
        print "Exception Handled Successfully : ", e
l = ListDemo()
list1 = raw_input("Enter the elements: ").split(" ")
l.setList(list1)
l.getList()
element = int(raw_input("Enter the index of element to remove: "))
l.removeList(element)