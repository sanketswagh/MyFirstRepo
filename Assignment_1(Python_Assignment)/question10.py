# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:24:32 2017

@author: Sanket Wagh
"""
import pytz
import datetime

gmt = pytz.timezone('GMT')
eastern = pytz.timezone('US/Eastern')

time = "Tue, 11 Oct 2017 15:38:10 GMT"

date = datetime.datetime.strptime(time, '%a, %d %b %Y %H:%M:%S GMT')

dategmt = gmt.localize(date)

dateeastern = dategmt.astimezone(eastern)
dateindian = dategmt.astimezone(gmt)

print "IST format (GMT): ",dateindian
print "US format(EST): ",dateeastern