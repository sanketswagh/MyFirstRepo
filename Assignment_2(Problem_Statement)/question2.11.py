# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:07:55 2017

@author: Sanket Wagh
"""

pattern="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
            pattern=pattern+"* "    
        else:      
            pattern=pattern+"  "    
    pattern=pattern+"\n"    
print(pattern)