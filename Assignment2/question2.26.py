# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:08:12 2017

@author: Sanket Wagh
"""


class MyExceptionClass(Exception):

    def __init__(self, arg):
        self.arg = arg

error = MyExceptionClass("Custom Exception Occurred")
raise error