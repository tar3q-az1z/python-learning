# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 23:41:31 2022

@author: Md. Tareq Aziz
"""

x = "i am a string"
def check():
    x = 3
    print("inside function, x = ", x)
print("outside function, x = ", x)
check()
print("outside function, x = ", x)