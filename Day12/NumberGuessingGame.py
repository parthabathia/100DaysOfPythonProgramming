from NumberGuessingGameArt import logo
import random
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == 'easy':
        return EASY_LEVEL_TURNS
    else : 
        return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
    """Checks answer against guess. Retruns the number of turns returning."""
    if guess > answer:
        print("Too high.")
        return turns-1
    elif guess < answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}.")

def play_game():
    print(logo)
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have exhausted all the guesses. Game over. You lost.")
            return 0


while input("Do you want to play the Number Guessing Game? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    play_game()
else:
    print("Sorry to see you go.")
    



