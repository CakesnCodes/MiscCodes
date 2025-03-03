# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:56:13 2024

@author: User
"""

#Exercise (Temperature switcharoo)
#maybe you could try converting the temperature either way?

def f_to_c(f):
     c = ((f-32) * 5) / 9
     round(c,2)
     print (f" {f} °F is {c} °C")

def c_to_f(c):
    f = (c * 1.8) + 32
    round(f,2)
    print (f" {c} °C is {f} °F")


try:
    temp=int(input("""
        What scale do you want to convert your temperature into?
              
            [1] Celsius -> Fahrenheit
            [2] Fahrenheit -> Celsius 
              
              """))
              
    if temp == 1:
        c = float(input("Input temperature: "))
        c_to_f(c)
        
    elif temp == 2:
        f = float(input("Input Temperature: "))
        f_to_c(f)

except:
    print("Invalid input")