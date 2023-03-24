# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:59:27 2022

@author: Md. Tareq Aziz
"""

try:
    number = int(input())
    print(number)
except ValueError:
    print("please input a valid number")