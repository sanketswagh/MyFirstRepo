# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:42:28 2017

@author: Sanket Wagh
"""

import re

value = []
data=[x for x in raw_input("Enter the password to check: ").split(',')]
for i in data:
    if len(i)<6 or len(i)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",i):
        continue
    elif not re.search("[0-9]",i):
        continue
    elif not re.search("[A-Z]",i):
        continue
    elif not re.search("[$#@]",i):
        continue
    elif re.search("\s",i):
        continue
    else:
        pass
    value.append(i)
print "Valid Password: ",
print ",".join(value)