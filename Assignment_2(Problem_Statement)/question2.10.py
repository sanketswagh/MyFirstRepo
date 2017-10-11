# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:06:36 2017

@author: Sanket Wagh
"""

pattern="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or (row == 6 and column != 0 and column < 6)):  
            pattern=pattern+"*"    
        else:      
            pattern=pattern+" "    
    pattern=pattern+"\n"    
print(pattern)