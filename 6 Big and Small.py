# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:40:49 2024

@author: User
"""
# Exercise 5 (Big and small)

seeit = [5,3,2,2,23,10,15,20]

print (f"""
Current list:
    {seeit}  
       """) #say it

seeit.sort() #sorted
longeth= len(seeit)

print (f"Lowest number: {seeit[0]} \nHighest number: {seeit[longeth-1]}")