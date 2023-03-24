# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 23:54:37 2022

@author: Md. Tareq Aziz
"""

x = 11
def out_scope():
    y = 13
    def inner_scope():
        z = x + y
        return z
    return inner_scope()
print(out_scope())