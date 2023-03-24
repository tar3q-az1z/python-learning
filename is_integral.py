# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 22:52:05 2022

@author: Md. Tareq Aziz
"""

# only for floating value 
x = 2.5
print(x.is_integer())  # returns false as it contains fraction
x = 10.0000000
print(x.is_integer())  # returns true as it doesn't contain fraction, actually it is an integer
