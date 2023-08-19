##################### Extra Hard Starting Project ######################
from datetime import datetime
import smtplib
import pandas
import random
from secret import *

FILES_PATH = "Day 32 - SMTP & DateTime/birthday-wisher/letter_templates/"
FILES = ["letter_1", "letter_2", "letter_3"]

PLACEHOLDER = "[NAME]"

GMAIL_HOST = "smtp.gmail.com"


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()
month = now.month
day = now.day


birthday_file = pandas.read_csv("Day 32 - SMTP & DateTime/birthday-wisher/birthdays.csv")

month_data = birthday_file["month"].to_list()
people = birthday_file[birthday_file.month == month][birthday_file.day == day]
names = people["name"].to_list()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for name in names:
    user_data = people[people.name == name]
    user_email = user_data["email"]
    with open(file = f"{FILES_PATH}{random.choice(FILES)}.txt") as letter:
        letter_content = letter.read()
        email_body = letter_content.replace(PLACEHOLDER,name)

        with smtplib.SMTP(GMAIL_HOST) as connection:
            connection.starttls()
            connection.login(user = my_email, password = my_password)
            connection.sendmail(
                from_addr = my_email,
                to_addrs = user_email,
                msg = f"Subject:Happy Birthday\n\n{email_body}"
                )
            print(f"Sent Birthday wishes to {name}.")



# 4. Send the letter generated in step 3 to that person's email address.




