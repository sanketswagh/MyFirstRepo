# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 15:13:49 2017

@author: Sanket Wagh
"""
import re
class PasswordValidity:
    try:    
        def validate(password):
            pwd = password;
            if re.match(r'[A-Za-z0-9$#@]{6,12}', pwd):
                print "Valid Password"
            else:
                print "Invalid Password"
            return;
            
        def main():
            print "Password Validity Check"
        if __name__ == "__main__":
            main()
        password = raw_input("Enter your password to test: ")
        validate(password)
            
    except Exception, e:
        print "Exception Handled Successfully : ", e
        