import os
import datetime as dt
import smtplib
import random

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
TO_ADDRS = os.environ.get("TO_ADDRS")

day_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#get the day of the week of today
today_of_the_week = dt.datetime.now().weekday()

#to obtain a list of quotes from quotes.txt
with open(file="quotes.txt") as file:
    quotes = file.readlines()

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=TO_ADDRS,
        msg=f"Subject: Happy {day_of_the_week[today_of_the_week]}\n\n {random.choice(quotes)}"
    )
print("Email sent successfully!")
