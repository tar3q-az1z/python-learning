# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 01:00:55 2022

@author: Md. Tareq Aziz
"""

total = 9
def add(n):
    global total
    total = total + n
add(10)
print(total)