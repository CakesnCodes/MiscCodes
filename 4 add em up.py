# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:05:04 2024

@author: User
"""
total= 0

while True:
    try:
        num = input("Input number (Must be positive): ")
        for d in str(num):      
            num1 = int(d)
            total += num1

        print(total)
        break
        
    except Exception:
        print("")