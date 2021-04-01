#!/usr/bin/env python

import random

def main():
    """Start a number guessing game between 1 to 100"""
    print("Guess the number")

    x = random.randrange(1 , 100)
    print(x)
    guess = None

    while x != guess:

        guess = int(input("Pick a number between 1 to 100: "))

        if x == guess:
            print("You genius!")
            break
        else:
            print("Sorry try again")

main()
