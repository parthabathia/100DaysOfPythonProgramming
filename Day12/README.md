# Day 12 of Python programming bootcamp

The provided code is a Python script for a Number Guessing Game. Here's a description of the code:

1. The code imports the logo and necessary modules (`random` and `os`) from a module named `NumberGuessingGameArt`.
2. It defines constants `EASY_LEVEL_TURNS` and `HARD_LEVEL_TURNS` representing the number of turns allowed for easy and hard difficulty levels.
3. The function `set_difficulty()` prompts the user to choose a difficulty level ('easy' or 'hard') and returns the corresponding number of turns based on the chosen difficulty.
4. The function `check_answer(guess, answer, turns)` compares the user's guess against the randomly generated answer and provides feedback. It returns the updated number of turns.
5. The function `play_game()` initializes the game by printing the logo and a welcome message. It generates a random number between 1 and 100 as the answer and allows the user a certain number of turns based on the chosen difficulty. The user is prompted to guess the number, and the game continues until the user guesses correctly or runs out of turns.
6. The main part of the script uses a `while` loop to repeatedly ask the user if they want to play the game. If the user chooses to play ('y'), the game is played by calling the `play_game()` function. If the user chooses not to play ('n'), the loop exits, and a farewell message is displayed.

Note: The script uses the `os.system('cls')` command to clear the console screen, which is specific to Windows systems. If you are using a different operating system, you might need to modify this part of the code.