# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:57:28 2022

@author: Md. Tareq Aziz
"""

def checkReturn():
    print("i am before return statement!")
    return  # as soon as return noticed, function stops running
    print("i am after return statement!")
    
checkReturn()