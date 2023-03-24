# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 18:08:28 2022

@author: Md. Tareq Aziz
"""

def divide(n1, n2):
    try:
        return n1 / n2
    #except (TypeError, ZeroDivisionError):
        #print("encountered a problem")
    except TypeError:
        print("both should be integral number.")
    except ZeroDivisionError:
        print("n2 can't be zero.")

try:
    n1 = float(input())
    n2 = float(input())
    print(divide(n1, n2))
except ValueError:
    print("enter a number")