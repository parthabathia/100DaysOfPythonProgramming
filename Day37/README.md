# Day 37 of Python programming bootcamp

This Python script interacts with the Pixela API, a service for tracking habits and activities over time through graphs. Here's a breakdown of what each section does:

1. **Importing Libraries**: 
    - `requests`: Necessary for making HTTP requests to the API.
    - `datetime`: Used to get the current date and time.

2. **Setting up User and Authentication Information**:
    - `username`: Your Pixela username.
    - `token`: Your Pixela authentication token.

3. **Creating a New User Profile**:
    - Sends a POST request to the Pixela API to create a new user profile.
    - Includes user parameters like username, token, agreement to terms of service, and age verification.

4. **Creating a Graph Definition**:
    - Sends a POST request to create a new graph for tracking.
    - Specifies parameters like graph ID, name, unit (e.g., commits), type (e.g., integer), and color.

5. **Adding a Pixel to the Graph**:
    - Sends a POST request to add a new data point (pixel) to the graph.
    - Uses the current date and a quantity (e.g., number of commits) as parameters.

6. **Updating a Pixel's Quantity**:
    - Sends a PUT request to update the quantity of a specific pixel on the graph for a given date.
    - Uses the graph ID, date, and new quantity as parameters.

7. **Deleting a Pixel**:
    - Sends a DELETE request to remove a specific pixel from the graph for a given date.
    - Uses the graph ID and date as parameters.

This script demonstrates basic interactions with the Pixela API, including user profile creation, graph setup, pixel addition, updating, and deletion.