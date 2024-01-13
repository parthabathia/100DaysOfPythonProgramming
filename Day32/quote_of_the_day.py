import smtplib
import random
import datetime

WEEKDAY = datetime.datetime.now().weekday()
EMAIL = "abc@xyz.com"
PASSWORD = "abcdefghijklmnop" # Generate an App Password from your Google Account


def get_quote():
    try:
        with open("quotes.txt", mode="r") as file:
            all_quotes = file.readlines()
    except FileNotFoundError:
        pass
    else:
        return random.choice(all_quotes)


def send_email(list_of_emails):
    if WEEKDAY == 1:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            for email in list_of_emails:
                connection.sendmail(
                    from_addr=PASSWORD,
                    to_addrs=email,
                    msg=f"Subject: Quote of the Day\n\n{get_quote()}"
                )


list_of_emails = ["abc@xyz.com", "xyz@abc.com"]
send_email(list_of_emails)
