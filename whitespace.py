# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 00:20:44 2022

@author: Md. Tareq Aziz
"""

# rstrip() for removing whitesapce from right side
# but they don't change the main string
string = "i am from bd     "
print("len before strip :", len(string))
print("len after strip: ", len(string.rstrip()))

print("----------------------------")

# lstrip() for removing whitesapce from left side
# but they don't change the main string

string = "     Halda is a beautiful river."
print(string)
print(string.lstrip())

print("----------------------------")

# strip() used for removing whitespace from both sides of string
# but they don't change the main string

string = "   Aziz   "
print("len before: ", len(string))
print(string.strip())
print("len after: ", len(string.strip()))
