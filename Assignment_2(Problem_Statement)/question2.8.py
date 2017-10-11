# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:44:22 2017

@author: Sanket Wagh
"""
pattern="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
            pattern=pattern+"*"    
        else:      
            pattern=pattern+" "    
    pattern=pattern+"\n"    
print(pattern)