# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 02:04:04 2022

@author: Md. Tareq Aziz
"""

string = "it was circle and bound by circle"
print(string.find("circle"))
print(string.replace("circle", "line"))
print(string)  # so .replace() creates a copy only
# to change it
string = string.replace("circle", "line")
print(string)