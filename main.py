import os
import pandas as pd
import datetime as dt
import smtplib
import random

letters = ["letter_1", "letter_2", "letter_3"]
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
time = dt.datetime.now()
with open("birthdays.csv", "r") as file:
    data = pd.read_csv(file)
    for index, row in data.iterrows():
        if time.month == row.month and time.day == row.day:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                wish_letter = random.choice(letters)
                with open("./letter_templates/" + wish_letter + ".txt", "r") as f:
                    content = f.read()
                    new_content = content.replace("[NAME]", row["name"])

                connection.sendmail(from_addr=MY_EMAIL, to_addrs=row.email, msg=f"Subject:Happy Birthday!\n\n{new_content}")
