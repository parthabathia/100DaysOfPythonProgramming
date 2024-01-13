import time
import requests
from datetime import datetime
import smtplib

MY_LAT = -36.204159
MY_LONG = -51.8516821


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    return iss_latitude, iss_longitude


def get_sunrise_sunset():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "UTC"
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    return sunrise, sunset


def is_iss_close():
    iss_latitude, iss_longitude = get_iss_position()
    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5 and MY_LONG + 5 >= iss_longitude >= MY_LONG - 5:
        return True
    return False


def send_email_notification():
    sunrise, sunset = get_sunrise_sunset()
    if is_iss_close() and (datetime.now().hour > sunset or datetime.now().hour < sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="ABC@XYZ.com", password='abcdefghijklmnop')
            connection.sendmail(
                from_addr="ABX@XYZ.com",
                to_addrs="XYZ@XYZ.com",
                msg="Subject: Look Up\n\nThe ISS is above you!!!"
            )


while True:
    time.sleep(60)
    send_email_notification()
