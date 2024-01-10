# Day 25 of Python programming bootcamp

This Python code creates an interactive U.S. States guessing game using the Turtle graphics library and the Pandas library for data manipulation. Here's a description of the code:

1. **Imports:**
   - `import pandas as pd`: Imports the Pandas library and aliases it as `pd` for ease of use.
   - `import turtle`: Imports the Turtle graphics library for creating a simple graphical interface.

2. **Setting up Turtle:**
   - `screen = turtle.Screen()`: Creates a Turtle graphics screen.
   - `screen.title("U.S. States Game")`: Sets the title of the Turtle graphics screen.
   - `screen.addshape("blank_states_img.gif")`: Adds a custom shape (U.S. map image) to be used by the Turtle.
   - `turtle.shape("blank_states_img.gif")`: Sets the shape of the Turtle to the U.S. map image.

3. **Loading U.S. States Data:**
   - `us_states = pd.read_csv("50_states.csv")`: Reads a CSV file ("50_states.csv") containing U.S. states data into a Pandas DataFrame.
   - `all_states = us_states["state"].tolist()`: Creates a list of all U.S. states from the DataFrame.

4. **Game Loop:**
   - `guessed_states = []`: Initializes an empty list to store the guessed states.
   - The while loop continues until all 50 states are guessed or the user types "Exit."
   - Inside the loop:
      - `answer_state = screen.textinput(...)`: Takes user input for guessing a state's name through a pop-up dialog.
      - If the user types "Exit," the loop breaks.
      - If the guessed state is correct, a Turtle is used to display the state name on its corresponding location on the U.S. map. The guessed state is then added to the `guessed_states` list.

5. **Processing States Not Guessed:**
   - `states_not_guessed = [state for state in all_states if state not in guessed_states]`: Creates a list of states that were not guessed.

6. **Creating DataFrame and Saving to CSV:**
   - `df = pd.DataFrame(states_not_guessed)`: Converts the list of states not guessed into a Pandas DataFrame.
   - `df.to_csv("states_to_learn.csv")`: Writes this DataFrame to a CSV file ("states_to_learn.csv") containing the states that the user did not guess correctly. This file can be used for further learning or practice.

In summary, this code allows users to guess U.S. states interactively on a map using Turtle graphics, and it keeps track of the states that were not guessed for additional practice.