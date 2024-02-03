# Day 38 of Python programming bootcamp

This code is designed to track your daily exercises and store them in a Google Sheet using the Nutritionix and Sheety APIs. Here's a breakdown of what each part does:

1. **Imports**: The code imports necessary modules like `requests` for making HTTP requests and `datetime` for handling dates and times.

2. **API Keys and Tokens**: It sets constants for Nutritionix API key and ID (`NUTRI_API_KEY` and `NUTRI_APP_ID`), and Sheety token (`SHEETY_TOKEN`). These are necessary for authentication with the respective APIs.

3. **Personal Information**: It defines constants for your gender, weight, height, and age, which are used as parameters when querying the Nutritionix API.

4. **User Input**: Asks the user to input which exercises they did today.

5. **Nutritionix API Call**: Constructs the request to the Nutritionix API with the provided query, gender, and age. It sends the request and retrieves exercise data in JSON format.

6. **Sheety API Endpoint**: Defines the endpoint for the Sheety API where the workout data will be sent.

7. **Loop Through Exercises**: Loops through each exercise in the retrieved data from Nutritionix.

8. **Prepare Sheet Inputs**: Formats the exercise data into a dictionary that matches the expected format by the Sheety API.

9. **Send to Sheety**: Sends a POST request to the Sheety API with the workout data for each exercise.

10. **Print Response**: Prints the response from Sheety, which likely includes information about the success or failure of the request.

Overall, this code automates the process of recording daily exercises into a Google Sheet, making it easier to track fitness progress over time.
