import datetime as dt
import smtplib
import random
my_email = "python100xtest@gmail.com"
my_email_password = "pggh tksa qccp btcn"
to_addrs = "python100_test@yahoo.com",

day_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#get the day of the week of today
today_of_the_week = dt.datetime.now().weekday()

#to obtain a list of quotes from quotes.txt
with open(file="quotes.txt") as file:
    quotes = file.readlines()

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_email_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_addrs,
        msg=f"Subject: Happy {day_of_the_week[today_of_the_week]}\n\n {random.choice(quotes)}"
    )
print("Email sent successfully!")