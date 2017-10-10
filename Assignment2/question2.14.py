# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:54:56 2017

@author: Sanket Wagh
"""

year = int(raw_input("Input a year: "))
if (year % 400 == 0):
    leapyear = True
elif (year % 100 == 0):
    leapyear = False
elif (year % 4 == 0):
    leapyear = True
else:
    leapyear = False

    
month = int(raw_input("Input a month [1-12]: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    monthlength = 31
elif month == 2:
    if leapyear:
        monthlength = 29
    else:
        monthlength = 28
elif month > 12:
    print "Invalid Input Please try again!!!"
else:
    monthlength = 30


day = int(raw_input("Input a day [1-31]: "))
if day < monthlength:
    day += 1
elif day > 31:
    print "Invalid Input Please try again!!!"
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))