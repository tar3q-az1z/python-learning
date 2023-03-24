# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:04:57 2022

@author: Md. Tareq Aziz
"""

s1 = "Tareq"
s2 = "aziz"
s3 = s1 + " " + s2
print(s3)
print(s3[-1])
print(s3[-2])
print(s3[-len(s3)])  # first char of s3
print(s3[:6])
print(s3[6:])
print(s3[:])
print(s3[6:20])
print(s3[50:100])  # prints nothing
print(s3[-6:-2])
print(s3[-6:0])
print(s3[-6:])
