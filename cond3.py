# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:56:59 2022

@author: Md. Tareq Aziz
"""

n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
print(count)