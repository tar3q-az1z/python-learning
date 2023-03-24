# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 10:34:16 2022

@author: Md. Tareq Aziz
"""

a_point = 3.0, 4.5, 5.5  # omitted parentheses, valid 
print(type(a_point))  # a tuple
print(a_point)
print(4.5 in a_point)  # existence
x, y, z = a_point  # unpacking
print("x = ", x)
print("y = ", y)
print("z = ", z)
a, b, c = 2, "literal", 3.5  # mul. var. assignment using tuple
print(c)
