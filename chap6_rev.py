# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 07:30:08 2023

@author: Md. Tareq Aziz
"""

n = 1
while n <= 5:
    print(n)
    n += 1
for letter in "python":
    print(3)

total = 0
def addd(n):
    global total
    total += n
    return total
print(addd(5))

print(True or False)