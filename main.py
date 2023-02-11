import random

NUM_OF_DIGITS = 3
MAX_NUM_OF_GUESSES = 10

def main():
    print(f"I'm thinking of a {NUM_OF_DIGITS} digit number with no repeated numbers.")
    print("Try to guess what it is!\nHere are some clues. When I say:")
    print("'Pico'   that means: One digit is correct but in the wrong position.")
    print("'Fermi'  that means: One digit is correct and in the right position.")
    print("'Bagels' that means: No digit is correct.")
    print("For example: if the secret number is 248 and your guess was 843, the clues would be Fermi Pico.")



if __name__ == "__main__":
    main()