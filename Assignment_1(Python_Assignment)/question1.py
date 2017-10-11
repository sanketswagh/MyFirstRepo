# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 10:40:29 2017

@author: Sanket Wagh
"""

#import logging
#LOG_FILENAME = 'question1.log'
#logging.basicConfig(filename=LOG_FILENAME,level=logging.debug)
try: 
    raise RuntimeError('Runtime Exception Occurred...1') 
except RuntimeError:
    print 'Runtime Exception Handled...'
    raise RuntimeError('Runtime Exception Occurred...2')
#    logging.debug(10,"Exception logged successfully!!!")
#else:
#    print "No Exception Occurred."