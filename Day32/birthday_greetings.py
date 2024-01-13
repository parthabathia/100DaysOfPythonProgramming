import random
import datetime as dt
import smtplib
import glob
import pandas as pd

DAY_TODAY = dt.datetime.now().day
MONTH_TODAY = dt.datetime.now().month
EMAIL = "abc@xyz.com"
PASSWORD = "abcdefghijklmnop" # Generate an App Password from Google Account


def get_letter_template():
    """Get a random birthday template."""
    txt_files = [file for file in glob.glob("./letter_templates/*.txt")]
    letter_templates = []
    for file in txt_files:
        with open(file, mode="r") as template:
            letter_templates.append(template.read())

    return random.choice(letter_templates)


def get_list_of_people():
    """Get a list of people whose birthday is today."""
    list_of_people = pd.read_csv("birthday_list.csv")
    birthday_today = [people for people in list_of_people.to_dict(orient="records")
                      if people['month'] == MONTH_TODAY and people['day'] == DAY_TODAY]
    return birthday_today


def prepare_letter(name):
    """Get a customised letter with the name of the person whose birthday is today."""
    template = get_letter_template()
    letter = template.replace("[NAME]", name)
    return letter


def send_greetings():
    """Send a birthday greeting."""
    list_of_people = get_list_of_people()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        for people in list_of_people:
            name = people['name']
            email = people['email']
            letter = prepare_letter(name)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=email,
                msg=f"Subject: Happy Birthday!\n\n{letter}"
            )


send_greetings()
