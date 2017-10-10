# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 16:27:51 2017

@author: Sanket Wagh
"""
#import pytz
import datetime
#gmt = pytz.timezone('GMT')

currentdatetime = datetime.datetime.now()
#time = currentdatetime
#date = datetime.datetime.strptime(time, '%a, %d %b %Y %H:%M:%S GMT')
print("Current date & time(IST): ",currentdatetime)


#eastern = pytz.timezone('US/Eastern')
#time = currentdatetime
#date = datetime.datetime.strptime(time, '%a, %d %b %Y %H:%M:%S GMT')
#dategmt = gmt.localize(date)
#dateeastern = dategmt.astimezone(eastern)
