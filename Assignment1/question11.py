# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 17:02:28 2017

@author: Sanket Wagh
"""

class AdditiveSequenceCheck:
    try:    
        def additiveSequence(seq,nTerm):
                
              list1 = [int(i) for i in str(seq)]
              
              x = list1[0]
              y = list1[1]
              print x,
              while(y <= nTerm):
                  print y,
                  x,y = y,x+y                                
              return
            
        def main():
            print "Additive Sequence check"
        if __name__ == "__main__":
            main()
        seq = raw_input("Enter the sequence: ")
        nTerm = input("Enter the Nth term: ")
        additiveSequence(seq,nTerm)
            
    except Exception, e:
        print "Exception Handled Successfully : ", e
        