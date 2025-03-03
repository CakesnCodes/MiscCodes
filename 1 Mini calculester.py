# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:49:01 2024

@author: User
"""

#Exercise 1 (Mini Calculester)

while True:
    try:
        a=int(input("Input first number: "))
        b=int(input("Input second number: "))
        break    
    except Exception:
        print("Invalid input")
        
print(" ")
print(f"Addition \n {a} + {b} = {a+b}")
print(" ")
print(f"Subtraction \n {a} - {b} = {a-b}")
print(" ")
print(f"Multiplication \n {a} * {b} = {a*b}")
print(" ")
print(f"Division \n {a} / {b} = {a/b}")