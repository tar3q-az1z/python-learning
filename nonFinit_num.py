# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 15:34:57 2022

@author: Md. Tareq Aziz
"""

num = 1_0000_000  # easy to detect or read
print(num)

# don't care about memory in python
# python can handle any large number
num = 10000000000000000000000000000000000000000000000000000000000000000
print(len(str(num)))
print(num)

# float representation
num = 1000.0
print(num)
num = 1_000.0
print(num)
num = 1e3  # exponential or scientific noation
print(num)
num = 1e-3
print(num)
print(1e300)
print(1e400)  # max range of float reaches