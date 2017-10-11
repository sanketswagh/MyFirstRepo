# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:35:30 2017

@author: Sanket Wagh
"""
import datetime
import logging
class AdditiveSequenceCheck:
    try:    
        def additiveSequence(seq,nTerm):
                
              list1 = [int(i) for i in str(seq)]
#             if (not (list1[i]==list1[i+1]==0)):
              x = list1[0]
              y = list1[1]
              print "Additive sequence is: ",x,
              while(y <= nTerm):
                  print y,
                  x,y = y,x+y  
              return
#             else: 
#                 print "Not a additive sequence"
              
            
        def main():
            print "Additive Sequence check"
        if __name__ == "__main__":
            main()
        
        seq = raw_input("Enter the sequence: ")
        nTerm = input("Enter the Nth term: ")
        additiveSequence(seq,nTerm)
        
        currentdatetime = datetime.datetime.now()
        logging.basicConfig(filename='C:\Program Files\Git\MyFirstRepo\Assignment1\question12.log',filemode='w',level=logging.DEBUG)
        logging.debug('This message should go to the log file',currentdatetime)
        logging.warning('Entry made into log file....!!!')
            
    except Exception, e:
        print "Exception Handled Successfully : ", e