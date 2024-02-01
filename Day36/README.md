# Day 36 of Python programming bootcamp

This Python script retrieves stock data for Tesla Inc (ticker symbol: TSLA) from the Alpha Vantage API and then fetches recent news related to Tesla from the News API. It calculates the difference in stock prices between yesterday and the day before yesterday, determines whether the stock has gone up or down, and sends a message containing the stock performance and headlines of recent news articles via Twilio SMS.

1. It imports the necessary libraries: `requests` for making HTTP requests and `twilio.rest` for interacting with the Twilio API.

2. Defines constants for Twilio account SID, authentication token, stock symbol, company name, Alpha Vantage API key, and News API key.

3. Defines the `check_stock()` function:
   - Constructs the endpoint and parameters for the Alpha Vantage API to retrieve daily stock data.
   - Retrieves stock data, calculates the difference in closing prices between yesterday and the day before yesterday, and determines whether the stock has gone up or down.
   - If the difference percentage is greater than 1, it calls the `get_news()` function to fetch recent news articles and then calls the `send_message()` function to send the news and stock performance via SMS.

4. Defines the `get_news()` function:
   - Constructs the endpoint and parameters for the News API to fetch news articles related to Tesla.
   - Retrieves news data and returns the top 3 articles.

5. Defines the `send_message()` function:
   - Formats the news articles and stock performance into a readable message.
   - Uses the Twilio client to send SMS messages containing the formatted data.

6. Calls the `check_stock()` function to execute the script.

Note: You need to replace placeholders like "your_account_sid", "your_auth_token", "your_api_key", "temp_number", and "your_number" with your actual Twilio credentials, Alpha Vantage API key, and phone numbers before running the script.