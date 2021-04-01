import random
import math

def main():
    """Start a number guessing game between 1 - 100."""
    print("Guess the number!")
    x = math.floor(random.triangular(-1000, 1000, 1))
    guess = None
    while x != guess:
        guess = int(input("Pick a number between -1000 to 1000: "))

        if x == guess:
           print("You genius!")
           break

        else:
            print("Failure. Try Again. the correct ans was:" + str(x))
            break


main()