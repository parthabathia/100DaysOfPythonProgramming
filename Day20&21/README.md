# Day 20 & 21 of Python programming bootcamp

This Python code is a simple implementation of the classic Snake game using the Turtle graphics library. The game involves controlling a snake on a graphical window and attempting to eat food while avoiding collisions with the walls and the snake's own tail.

Here's a breakdown of the code:

1. **Importing Modules:**
   - The code imports necessary modules: `Screen` from the Turtle library, and custom modules `Snake`, `Food`, and `Scoreboard`. Additionally, the `time` module is imported for introducing delays in the game loop.

2. **Setting up the Screen:**
   - The Turtle screen is created with a width and height of 600 pixels. The background color is set to black, and the window title is set to "My Snake Game." The screen's update is turned off initially.

3. **Creating Snake, Food, and Scoreboard:**
   - Instances of the `Snake`, `Food`, and `Scoreboard` classes are created.

4. **Setting up Keyboard Input:**
   - Event listeners are set up to respond to arrow key presses, which control the snake's movement (up, down, left, right).

5. **Game Loop:**
   - The game loop (`while game_is_on:`) is where the main logic of the game occurs. The loop updates the screen, moves the snake, and checks for collisions.

6. **Collision Detection:**
   - Collision with food is detected when the snake's head is close to the food. If a collision occurs, the food is refreshed, the snake grows, and the player's score is increased.

   - Collision with the walls is detected by checking if the snake's head position exceeds the predefined boundaries. If a collision with the walls occurs, the game ends, and the "game over" message is displayed on the scoreboard.

   - Collision with the snake's own tail is checked by iterating over the snake's segments and comparing the distance between the head and each segment. If a collision with the tail is detected, the game ends, and the "game over" message is displayed.

7. **Exiting the Game:**
   - The game loop continues until `game_is_on` becomes `False`. After the loop, the screen is set to exit on click.

This code represents a basic structure for a Snake game using the Turtle graphics library, making it suitable for educational purposes or as a starting point for further development.