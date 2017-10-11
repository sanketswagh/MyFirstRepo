# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 14:46:04 2017

@author: Sanket Wagh
"""

class MyException(Exception):
   def __init__(self, value):
      self.value = value
   def __str__(self):
      return(repr(self.value))
      
   try:
     raise MyException("Exception is created by sanket wagh")
   except MyException as error:
     print ("A new exception raised and handled successfully :- ", error.value)