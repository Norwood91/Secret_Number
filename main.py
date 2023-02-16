import random

NUM_OF_DIGITS_FOR_SECR_NUM = 3
MAX_NUM_OF_GUESSES = 10

def main():
    print(f"I'm thinking of a {NUM_OF_DIGITS_FOR_SECR_NUM} digit number with no repeated numbers.")
    print("Try to guess what it is!\nHere are some clues. When I say:")
    print("'Pico'   that means: One digit is correct but in the wrong position.")
    print("'Fermi'  that means: One digit is correct and in the right position.")
    print("'Bagels' that means: No digit is correct.")
    print("For example: if the secret number is 248 and your guess was 843, the clues would be Fermi Pico.")

    while True: #main game loop
        num_to_guess = getSecretNum()
        print('I have a number in mind.')
        print(f'You have {MAX_NUM_OF_GUESSES} guesses.')

        num_of_guesses = 1
        while num_of_guesses <= MAX_NUM_OF_GUESSES:
            guess = ''
            #keep looping until they enter a valid guess
            while len(guess) != NUM_OF_DIGITS_FOR_SECR_NUM or not guess.isdecimal():
                print(f'Guess number: {num_of_guesses}')
                guess = input('> ')

            clues = getClues(guess, num_to_guess)
            print(clues)
            num_of_guesses += 1

            if guess == num_to_guess:
                print('You guessed correctly! You WIN!')
                break # They're correct, so break out of the loop
            if num_of_guesses > MAX_NUM_OF_GUESSES:
                print('You ran out of guesses... You LOSE!')
                print(f'The answer was {num_to_guess}')

        # Ask player if they want to play again
        play_again = input('Do you want to play again? Type yes or no').lower()
        if play_again != 'yes':
            break
        print('Thanks for playing! See you next time!')












if __name__ == "__main__":
    main()