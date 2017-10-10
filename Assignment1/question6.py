# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 13:23:09 2017

@author: Sanket Wagh
"""
import re   
try:
    EmailID = "sanket.wagh@quantiphi.com"
    regex = r'^([^@]+)'
    regex1 = r'@([\w.]+)\.'       
    username = re.search(regex,EmailID) 
    companyname = re.search(regex1,EmailID) 
    print "Username : ",username.group()
    print "Companyname : ",companyname.group(1)
except Exception, e:
    print "Exception Handled Successfully : ", e