# Day 11 of Python programming bootcamp

The provided Python code implements a simple text-based version of the game Blackjack. Here's a description of the code:

1. **Import Statements:**
   - `BlackjackArt`: The code imports a module named `BlackjackArt` that likely contains ASCII art for the game's logo.
   - `random`: Used for generating random numbers (for dealing cards).
   - `system` from the `os` module: Used to clear the console screen.

2. **Functions:**
   - `deal_card()`: Returns a random card value from a standard deck of cards (with values 2 to 11).
   - `calculate_score(cards)`: Takes a list of cards and returns the total score. It handles the special case of an Ace being worth 1 or 11 based on the total score.
   - `compare(user_score, computer_score)`: Compares the final scores of the player and the computer and determines the outcome (win, lose, draw, or blackjack).
   - `play_game()`: Implements the main game logic. It initializes the game, deals cards to the player and computer, allows the player to draw additional cards, and calculates the final scores.

3. **Game Execution:**
   - The game starts by displaying the Blackjack logo.
   - The player and the computer are dealt two cards each.
   - The player is prompted to draw additional cards ("y" for yes, "n" for no) until they choose to pass or go over 21.
   - The computer then automatically draws cards until it reaches a score of at least 17.
   - The final hands and scores are displayed, and the winner is determined using the `compare` function.

4. **Game Loop:**
   - The game is played repeatedly as long as the player chooses to play again (enters 'y' when prompted).

5. **Console Clearing:**
   - The `system('cls')` statement clears the console screen at the beginning of each game, providing a cleaner interface.

The game provides a simple but functional text-based Blackjack experience, allowing players to interactively play the game and see the outcome.