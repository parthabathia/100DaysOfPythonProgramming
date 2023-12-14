# Day 7 of Python programming bootcamp

This repository contain a Python code that implements a classic game of Hangman. Here's a breakdown of its functionality:

1. Setup:

    Imports necessary modules for words, hangman stages, and logo.
    Prints the game logo and initializes lives based on the number of hangman stages.
    Selects a random word from the word list and prints it (for debugging purposes).
    Initializes empty lists for guessed letters and displayed word blanks.

2. Gameplay Loop:

    Checks if the displayed word matches the chosen word or if lives are depleted (game over).
    Prompts the user to guess a letter (converted to lowercase).
    Prevents repeated guesses by checking if the letter is already used.
    Updates the "displayed word" by replacing blanks with guessed letters at their correct positions.
    Provides feedback for incorrect guesses by displaying the chosen stage and remaining lives.

3. Win/Lose Conditions:

    Winning: The displayed word matches the chosen word (user wins).
    Losing: Lives are depleted before the word is guessed (user loses).

Overall, this code provides a basic Hangman game with features like:

    Random word selection
    Tracking guessed letters
    Visual hangman stages for remaining lives
    Win/lose conditions with feedback

Feel free to explore and play around with the code. All the dependencies are also provided in the repository. Branch the code to improve on the overall mechanics or user experience.