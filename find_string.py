# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 23:59:48 2022

@author: Md. Tareq Aziz
"""

string = "world class topcoder"
print(string.find("class"))  # return index of first occurance
print(string.find("top"))
print(string.find("Top"))  # return -1 when substring no found
string = "line fine"
print(string.find("ine"))