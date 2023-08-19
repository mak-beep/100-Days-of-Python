import datetime as dt
import random
import smtplib
from secret import *
# print(my_email)

GMAIL_HOST = "smtp.gmail.com"


now = dt.datetime.now()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
day_of_week = now.weekday()
quote = ""
if (weekdays[day_of_week] == "Saturday"):
    with open("Day 32 - SMTP & DateTime\Birthday-Wisher\Birthday Wisher (Day 32) start\quotes.txt") as quote_file:
        quote_data = quote_file.readlines()
        quote = random.choice(quote_data)
        print(quote)

else:
    print("No motivation, Today.")


with smtplib.SMTP(GMAIL_HOST) as connection:
    connection.starttls()
    connection.login(user = my_email, password = my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="RECIEVER EMAIL",
        msg=f"Subject:Motivation\n\n{quote}"
        )

    