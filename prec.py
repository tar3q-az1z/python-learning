# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 19:14:33 2022

@author: Md. Tareq Aziz
"""

x = 2.3
print(round(x))
x = 2.7
print(round(x))
x = 2.5
print(round(x))  # unexpected behaviour when ends with 0.5
x = 3.5
print(round(x))  # but it is okay
x = 3.14159
print(round(x, 3))  # round upto 3 digits after decimal point
# print(round(x, 2.5)) # extra argument must be int
x = 2.675  # a tie
print(round(x, 2))  # should expect 2.68 but returns 2.67; a floating point error
