# Day 33 of Python programming bootcamp

## Directory Structure:

### 1. Email Notification with ISS Location and Sunrise-Sunset API
- **File**: `iss_tracker.py`
- **Description**: This Python program is designed to send email notifications using the SMTP protocol. It incorporates the International Space Station (ISS) location API and the Sunrise-Sunset API to determine whether the ISS is in proximity to the specified latitude and longitude during nighttime. If the ISS is within a certain degree range of the provided location, and it is nighttime, an email notification will be triggered.

#### Configuration:
- Update the email credentials, SMTP server details, and API keys in the script.
- Specify the target latitude and longitude for the location check.

#### How to Run:
```bash
python iss_email_notification.py
```

### 2. Kanye's Quotes Display
- **File**: `main.py`
- **Description**: This Python program utilizes the Kanye.rest API to fetch and display random quotes from Kanye West. The graphical user interface (GUI) is created using the Tkinter library, providing an interactive and visually appealing way to showcase Kanye's quotes.

#### How to Run:
```bash
python main.py
```

## Learning Highlights:
- **Kanye API Integration**: Understanding how to make HTTP requests to external APIs (Kanye.rest) and display the obtained data in a Tkinter-based GUI.
- **SMTP Email Sending**: Implementing email notifications using the SMTP protocol in Python.
- **ISS Location and Sunrise-Sunset API**: Incorporating real-time data from APIs to make informed decisions in the program logic.

## Notes:
- Ensure proper API key management and keep sensitive information secure.
- Test the email functionality with a disposable email or a dedicated testing account.
- Validate the program's functionality by checking ISS location and time zone considerations for accurate notifications.

This day's projects focus on practical applications, combining API integration, GUI development, and real-world scenarios with email notifications based on specific conditions.
