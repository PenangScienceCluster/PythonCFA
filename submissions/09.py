#!/usr/bin/env python

import random

def game():
    """Start a number guessing game between -100 - -1."""
    print("Guess the number!")

    n = random.randrange(-10, -1)
    # n = random.uniform(-10, -1) uniform returns a float number (not integer), so the number
    # would have decimals, basically impossible to guess
    # negative integers are ok but rmb it's from small to big numbers (1, 100 / -100, -1)
    # randint stands for random integers
    guess = None
    # print(n) to know the answer :) 

    while n != guess:
    # != means not equal to
        
        guess = int(input("Pick a number between -10 to -1: "))
        #int is to check if the number from player is an integer

        if n == guess:
            print("You genius!")
            break
        
        else:
            print("Try a different number")
game()