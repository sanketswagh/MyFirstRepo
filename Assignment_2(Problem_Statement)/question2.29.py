# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:34:33 2017

@author: Sanket Wagh
"""

TotalAmount = 0
while True:
    data = raw_input("Enter the data: ")
    if not data:
        break
    values = data.split(" ")
    check = values[0]
    amount = int(values[1])
    if check=="D":
        TotalAmount+=amount
    elif check=="W":
        TotalAmount-=amount
    else:
        pass
print "Total Balance: ",TotalAmount