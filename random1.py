# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 01:06:54 2022

@author: Md. Tareq Aziz
"""

import random 
def coin_flip():
    """ randomly returns head or tail"""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

tailsNo = 0
headsNo = 0
for trial in range(50_000):
    if(coin_flip() == "heads"):
        headsNo = headsNo + 1
    else:
        tailsNo = tailsNo + 1
print("P(heads): ", headsNo)
print("P(tails): ", tailsNo)
print(f"ratio: {headsNo / tailsNo: 0.2%}")