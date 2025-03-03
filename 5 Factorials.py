# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:23:42 2024

@author: User
"""
n = int(input("Input number: "))
fact = 1

for i in range(1, n+1):
    fact = fact * i

print(f"The factorial of {n} is: {fact}")
