Day 33 of 100-day Python coding challenge
# ISS Tracker & Email Notifier

This Python program tracks the International Space Station (ISS) and sends an email notification if the ISS is passing over your location during nighttime.

## Description

The program uses two APIs:
- The Open Notify API to get the current location of the ISS.
- The Sunrise-Sunset API to get the sunrise and sunset times for your location.

If the ISS is passing within a 5-degree range of your latitude and longitude, and it's nighttime (between sunset and sunrise), the program sends an email notification to alert you to look up and see the ISS.

## Installation

1. Install requests module:

```bash
pip install requests
```

2. Clone the repository:

```bash
git clone https://github.com/Ezzy401k/ISS_Tracker_and_Email_Notifier.git
```

3. Navigate to the project directory:

```bash
cd ISS_Tracker_and_Email_Notifier
```

## Usage

1. Run the program:

```bash
python ISS_Tracker_and_Email_Notifier.py
```

2. If the ISS is passing over your location during nighttime, you will be prompted to enter your email and password for authentication.

3. An email notification will be sent to alert you to look up and see the ISS.

## Author

[Esrael Mekdem](https://github.com/Ezzy401k)