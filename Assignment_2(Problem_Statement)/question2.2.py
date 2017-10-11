# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:58:22 2017

@author: Sanket Wagh
"""

temp = raw_input("Enter the  temperature in (C/F): ")
degree = int(temp[:-1])
temp1 = temp[-1]

if temp1.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  temp2 = "Fahrenheit"
elif temp1.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  temp2 = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", temp2, "is", result, "degrees.")