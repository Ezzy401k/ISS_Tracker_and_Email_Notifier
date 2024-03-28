import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MY_LAT = 8.564328 # Your latitude
MY_LONG = 39.289534 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

is_above = False

if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
    is_above = True

if is_above:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hr = time_now.hour

    if hr < sunrise or hr > sunset:
        my_email = input("Email: ")
        password = input("Password: ")

        message = MIMEMultipart()
        message["From"] = my_email
        message["To"] = my_email
        message["Subject"] = "Look Up!"

        body = "The ISS satelite is above you look up and see the marvelous station."

        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            # Log in to the sender's email account
            server.login(my_email, password)
            # Send the email
            server.sendmail(my_email, my_email, message.as_string())





