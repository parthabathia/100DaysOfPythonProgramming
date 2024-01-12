# Day 31 of Python programming bootcamp

This Python script uses the Tkinter library to create a simple French flashcard application with a graphical user interface. The flashcards contain French and English words, and the user is prompted to indicate whether they know the translation of a given word. The script reads data from a CSV file containing French words and their English translations, and the user can mark each word as known or unknown.

Here's a breakdown of the code:

1. **Importing Libraries:**
   - `tkinter`: Used for creating the graphical user interface.
   - `pandas`: Used for handling data in DataFrames.
   - `random`: Used for randomly selecting a flashcard.

2. **Global Variables:**
   - `BACKGROUND_COLOR`: Background color for the GUI.
   - `LANGUAGE_FONT`: Font configuration for language labels.
   - `WORD_FONT`: Font configuration for word labels.
   - `current_card`: A dictionary to store the current flashcard's data.

3. **Functions:**
   - `next_card()`: Displays the next flashcard or a completion message if all words are completed.
   - `is_right()`: Removes the current card from the data and saves the updated dataset to a CSV file.
   - `flip_card()`: Flips the flashcard to show the other side.
   - `all_complete()`: Displays a message when all words are completed and closes the window after a delay.
   - `close_window()`: Closes the Tkinter window.

4. **Reading Data:**
   - The script attempts to read a CSV file named "words_to_learn.csv." If the file is not found, it falls back to reading "french_words.csv."
   - If "words_to_learn.csv" is empty or an exception occurs, it reads "french_words.csv."
   - The data is converted to a dictionary for flashcard handling.

5. **Tkinter Window Setup:**
   - Creates a Tkinter window titled "French Flash Cards" with padding and background color.
   - Sets up a timer to flip the flashcard after 3 seconds.
   - Loads card images for the front and back of the flashcard.

6. **Canvas Setup:**
   - Creates a Tkinter canvas for displaying the flashcards.
   - Configures the canvas with a specified background color and no highlight thickness.
   - Places text elements for the language title and word on the canvas.

7. **Buttons Setup:**
   - Adds "Right" and "Wrong" buttons with corresponding images for user input.
   - Configures button actions to call `is_right()` and `next_card()` functions.

8. **Initializes the First Flashcard:**
   - Calls `next_card()` to display the first flashcard.

9. **Tkinter Main Loop:**
   - Starts the Tkinter main event loop to handle user interactions.

The application allows users to learn French words interactively by indicating whether they know the English translation of each word. The script incorporates visual elements, such as images and a graphical interface, to enhance the learning experience.