# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:02:18 2017

@author: Sanket Wagh
"""

string = raw_input("Input a string: ")
digit=letter=0
for count in string:
    if count.isdigit():
        digit=digit+1
    elif count.isalpha():
        letter=letter+1
    else:
        pass
print("Letters: ", letter)
print("Digits: ", digit)