# Day 22 of Python programming bootcamp

This Python code utilizes the Turtle graphics library to create a simple two-player Pong game. The game consists of two paddles, one on the left and one on the right, a ball that bounces around the screen, and a center line. The objective of each player is to prevent the ball from passing their paddle while trying to score points by making the ball pass the opponent's paddle.

Here's a breakdown of the main components:

1. **Turtle Setup:**
   - It imports the necessary modules from the Turtle library.
   - Creates a screen with a width of 1000, height of 600, a black background, and the title "My Snake Game."
   - The screen tracer is set to 0, disabling automatic updates to improve performance.
   - The screen listens for keyboard input.

2. **Game Objects:**
   - Two paddles (`paddle_left` and `paddle_right`) are created at specific positions using the `Paddle` class.
   - A ball (`ball`) is created using the `Ball` class.
   - A center line (`center_line`) is created using the `CenterLine` class.
   - Two scoreboards (`score_left` and `score_right`) are created to keep track of the players' scores.

3. **Keyboard Input:**
   - Event listeners are set up to respond to keyboard input.
   - Player on the right can move the paddle up and down using the "Up" and "Down" arrow keys.
   - Player on the left can move the paddle up and down using the "w" and "s" keys.

4. **Game Loop:**
   - The game loop (`while is_game_on:`) continuously updates the screen, moves the ball, and checks for collisions.
   - The ball's speed is controlled by the `time.sleep` function based on its `move_speed` attribute.
   - Conditions are checked for collisions with the top/bottom walls, paddles, and scoring zones.
   - If a player reaches a score of 5, the game announces the winner and exits the loop.

5. **Game Over:**
   - The game loop exits on a click event after one of the players reaches a score of 5.

This code provides a basic implementation of a Pong game using the Turtle graphics library and demonstrates fundamental concepts such as object-oriented programming, collision detection, and game loop mechanics.