# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:06:41 2022

@author: Md. Tareq Aziz
"""

count = 0
for i in range(1, 101):
    if(i % 2 == 0):
        break
    else:
        count = count + 1
print(count)