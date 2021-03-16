#!/usr/bin/env python

import random

def main():
    """Start a colour guessing game."""
    print("Guess the colour!")

    rainbow = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet"
        ]

    x = random.choice(rainbow)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What colour am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()