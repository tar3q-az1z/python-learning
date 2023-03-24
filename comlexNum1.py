# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 00:45:01 2022

@author: Md. Tareq Aziz
"""

n = 1 + 3j
print(n)
print(n.real)  # shows real part of n
print(n.imag)  # shows imaginary part of n
print(n.conjugate())  # shows the conjugate of n

print("---------------------------------------")
a = 3 + 4j
b = 11 - 2j
print(a + b)  # addition of com. var.
print(a - b)  #
print(a * b)
print(a / b)
print(a ** b)
# print(a // b)........ prohibited in python
print("-------------------")
x = 100
print("real and imag part of x is: ", x.real, " , ", x.imag)
print("conjugate of x: ", x.conjugate())