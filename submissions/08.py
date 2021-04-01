#!/usr/bin/env/python

import random

def main():
    """Start a numbern guessing game between 1 - 100."""
    print("Guess the number")
    
    x = random.randint( 1, 100 )
    guess = None
    
    while x != guess:

        guess = int ( input ("Pick a number between 1 to 100 : "))

        if x == guess:
            print("You genius!")
            break
        else:
            if x > guess:
                print("Try a bigger number")
            if x < guess:
                print("Try a smaller number")

main()   