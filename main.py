import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your latitude and longitude
MY_LAT = 8.564328
MY_LONG = 39.289534

# Fetch ISS position data from API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

# Extract ISS latitude and longitude
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Check if ISS is above your location
is_above = False
if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
    is_above = True

# If ISS is above your location
if is_above:
    # Parameters for fetching sunrise and sunset times
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # Fetch sunrise and sunset times
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get current hour
    time_now = datetime.now()
    hr = time_now.hour

    # Check if it's nighttime
    if hr < sunrise or hr > sunset:
        my_email = input("Email: ")
        password = input("Password: ")

        # Create email message
        message = MIMEMultipart()
        message["From"] = my_email
        message["To"] = my_email
        message["Subject"] = "Look Up!"

        body = "The ISS satellite is above you. Look up and see the marvelous station."

        message.attach(MIMEText(body, "plain"))

        # Send email notification
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(my_email, password)
            server.sendmail(my_email, my_email, message.as_string())
