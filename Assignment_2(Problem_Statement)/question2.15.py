# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:54:29 2017

@author: Sanket Wagh
"""
#
#Head Equation: r + c = 35
#Feet Equation: 4r+2c = 94
#-----------------------------
#Modify:
#2r + 2c = 70
#4r + 2c = 94
#--------
#
#Solve for "r":
#2r = 24
#r = 12 (# of rabbits)
#------------
#Solve for "c":
#r + c = 35
#12 + c = 35
#c = 23 (# of chickens)
heads = int(raw_input("Enter the number of heads: ")) # 35 heads
legs = int(raw_input("Enter the number of legs: "))   # 94 legs
for rabbits in range(heads+1):
    chickens = heads - rabbits
    if 2 * chickens + 4 * rabbits == legs:
        print ("Number of chickens are %d and number of rabbits are %d" %(chickens,rabbits))
        