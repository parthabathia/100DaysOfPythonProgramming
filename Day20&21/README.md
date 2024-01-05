# Day 20 & 21 of Python programming bootcamp

This Python code utilizes the Turtle graphics library to implement a simple Snake Game. Here's a description of the code:

1. **Importing Libraries:**
   - The code begins by importing necessary modules, including `turtle` for graphics, and custom classes (`Snake`, `Food`, `Scoreboard`) from separate files.

2. **Setting Up the Game Window:**
   - It creates a Turtle graphics window with dimensions 600x600, a black background, and the title "My Snake Game." The screen's update is turned off initially to enhance performance.

3. **Initializing Snake, Food, and Scoreboard:**
   - Instances of the `Snake`, `Food`, and `Scoreboard` classes are created for controlling the snake, placing food, and keeping score, respectively.

4. **Handling Keyboard Inputs:**
   - The program listens for arrow key inputs (`Up`, `Down`, `Left`, `Right`) to control the snake's movement.

5. **Main Game Loop:**
   - A while loop (`game_is_on`) controls the main game flow.
   - The screen is updated to reflect any changes in the game.
   - The snake moves with a slight delay (`time.sleep(0.1)`), creating the appearance of animation.

6. **Collision Detection:**
   - The code checks for three types of collisions:
      - Collision with food: If the snake's head touches the food, the food is refreshed, the snake grows longer, and the score is increased.
      - Collision with the wall: If the snake's head hits the game window boundaries, the game ends, and a "Game Over" message is displayed.
      - Collision with the snake's own tail: If the snake's head collides with any segment of its own tail, the game ends with a "Game Over" message.

7. **Play Again Prompt:**
   - After the game ends, a prompt is displayed asking if the player wants to play again (`Y` for Yes, `N` for No).
   - If the player chooses not to play again, the `play_again` variable is set to False, and the program exits.
   - If the player chooses to play again, the screen is cleared, and a new game starts.

Note: The game loop and user input handling continue until the player decides not to play again. The entire game is enclosed in a `while play_again` loop, allowing for multiple game sessions.