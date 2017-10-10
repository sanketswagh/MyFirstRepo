# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 18:48:54 2017

@author: Sanket Wagh
"""

list = [12,24,35,70,88,120,155]
list = [x for (i,x) in enumerate(list) if i not in (0,2,4,6)]
print(list)