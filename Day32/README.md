# Day 32 of python programming bootcamp

**Description: Automated Birthday Greetings Email Script**

The provided Python script automates the process of sending personalized birthday greetings via email. The script utilizes various libraries such as `random`, `datetime`, `smtplib`, `glob`, and `pandas` to achieve its functionality. Below is a breakdown of the key components and functionalities:

1. **Configuration:**
   - The current day and month are obtained using `datetime` to determine whose birthday it is today.
   - The email credentials (email address and password) are specified. It is recommended to generate an "App Password" from the Google Account for enhanced security.

```python
DAY_TODAY = dt.datetime.now().day
MONTH_TODAY = dt.datetime.now().month
EMAIL = "abc@xyz.com"
PASSWORD = "abcdefghijklmnop"  # Generate an App Password from Google Account
```

2. **Letter Template:**
   - The function `get_letter_template()` retrieves a random birthday template from a directory containing text files with templates. The templates are assumed to be in a folder named "letter_templates."

```python
def get_letter_template():
    """Get a random birthday template."""
    # ...
```

3. **Birthday List:**
   - The function `get_list_of_people()` reads a CSV file named "birthday_list.csv" using `pandas` and filters out individuals whose birthday matches the current date.

```python
def get_list_of_people():
    """Get a list of people whose birthday is today."""
    # ...
```

4. **Letter Preparation:**
   - The function `prepare_letter(name)` customizes the chosen letter template by replacing a placeholder `[NAME]` with the name of the person whose birthday it is.

```python
def prepare_letter(name):
    """Get a customised letter with the name of the person whose birthday is today."""
    # ...
```

5. **Email Sending:**
   - The main function `send_greetings()` retrieves the list of people with birthdays today, connects to the Gmail SMTP server, logs in, and sends personalized birthday emails using the `smtplib` library.

```python
def send_greetings():
    """Send a birthday greeting."""
    # ...
```

6. **Execution:**
   - The script concludes by invoking the `send_greetings()` function, triggering the entire process.

```python
send_greetings()
```

**Note:** Ensure that the script has the necessary permissions to access the CSV file, the letter templates directory, and the ability to send emails through the specified Gmail account. Additionally, consider using secure practices, such as storing credentials securely and using secure app passwords for email authentication.