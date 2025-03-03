# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:26:33 2024

@author: User
"""
act= ""
villagers= {"Aurora":"Penguin",
            "Bob":"Cat",
            "Carmen":"Rabbit",
            "Cherry":"dog",
            "Lolly":"Cat",
            "Marshal":"Squirrel",
            "Marina":"Squid",
            "Raymond":"Cat"}

for x, y in villagers.items():
    print(f"Name:{x} | Species:{y}")
    
while act != 4:
    try:
        act = int(input("""
        What would you like to do?
        [1] Add Villager
        [2] Replace Villager
        [3] Remove Villager
        [4] End program
              """))
              
        if act == 1:
            name = input("What's their name? ")
            species = input("What's their species? ")
        elif act == 2:
            replace= input("Who would you like to replace? ")
            name = input("What's their name of the new villager? ")
            species = input("What's their species? ")
        elif act == 3:
            remove = input("Who would you like to move away?")
            
            
        else:
            print("Invalid input")
    except Exception:
        print("Invalid input")