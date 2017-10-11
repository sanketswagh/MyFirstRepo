# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:18:17 2017

@author: Sanket Wagh
"""

import re
class PasswordValidity:
    try:    
        def validate(password):
            pwd = password;
#            ^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$
#           if re.match(r'[A-Za-z0-9$#@]{6,12}', pwd):
            if re.match(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z$#@s\d]{6,12}$', pwd):
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