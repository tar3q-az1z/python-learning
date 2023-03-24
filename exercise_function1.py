# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 01:38:39 2022

@author: Md. Tareq Aziz
"""

def celcius_to_farenheit(celcius):
    farenheit  = celcius * 9 / 5 + 32
    return farenheit
celcius = int(input())
print(f"{celcius} degree celcius = {celcius_to_farenheit(celcius)} degree farenheit")
