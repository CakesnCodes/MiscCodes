# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:52:23 2024

@author: User
"""

#Exercise 2 (Odd or Even)

while True:
    try:
        num=int(input("Input number: "))
        if num%2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
        break
    except Exception:
        print("Invalid input")