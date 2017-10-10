# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:24:29 2017

@author: Sanket Wagh
"""

import re   
try:
    EmailID = "sanket.wagh@quantiphi.com"
    regex = r'@([\w.]+)\.'       
    companyname = re.search(regex,EmailID) 
    print "Company Name : ",companyname.group(1)
except Exception, e:
    print "Exception Handled Successfully : ", e