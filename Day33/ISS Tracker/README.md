# Day 33 of Python programming bootcamp

This Python script is designed to periodically check the current position of the International Space Station (ISS) in relation to a specified location on Earth and send an email notification if the ISS is close to the given coordinates during nighttime.

Here's a breakdown of the code:

1. **Importing Libraries:**
   - `time`: Used for introducing delays between iterations.
   - `requests`: Used for making HTTP requests to retrieve data from APIs.
   - `datetime`: Used for handling date and time information.
   - `smtplib`: Used for sending emails.

2. **Constants:**
   - `MY_LAT` and `MY_LONG`: The latitude and longitude of the specified location on Earth.

3. **Functions:**
   - `get_iss_position()`: Retrieves the current latitude and longitude of the ISS using the Open Notify API.
   - `get_sunrise_sunset()`: Retrieves the sunrise and sunset times for the specified location using the Sunrise-Sunset API.
   - `is_iss_close()`: Checks if the ISS is within a proximity of ±5 degrees latitude and longitude of the specified location.
   - `send_email_notification()`: Sends an email notification if the ISS is close and the current time is during the night.

4. **Main Loop:**
   - The script enters an infinite loop using `while True`.
   - It sleeps for 60 seconds in each iteration (`time.sleep(60)`) to avoid making constant requests.
   - In each iteration, it calls `send_email_notification()` to check if the ISS is close and if it's nighttime. If both conditions are met, it sends an email notification.

5. **Email Notification:**
   - The email notification is sent using the Simple Mail Transfer Protocol (SMTP) via a Gmail server.
   - The email content includes a subject ("Look Up") and a message indicating that the ISS is above the specified location.

Note: To use this script, you need to replace the placeholder email addresses and password with your own Gmail credentials in the `send_email_notification()` function. Additionally, keep in mind that using hardcoded credentials in your code is generally not secure, and it's recommended to use environment variables or a more secure method for handling sensitive information.