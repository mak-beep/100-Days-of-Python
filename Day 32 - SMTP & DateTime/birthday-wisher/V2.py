from datetime import datetime
import smtplib
import pandas
import random
from secret import *

FILES_PATH = "Day 32 - SMTP & DateTime/birthday-wisher/letter_templates/"

PLACEHOLDER = "[NAME]"

GMAIL_HOST = "smtp.gmail.com"


now = datetime.now()
today = (now.month, now.day)
birthday_file = pandas.read_csv("Day 32 - SMTP & DateTime/birthday-wisher/birthdays.csv")

birthday_dict = {(data["month"], data["day"]): data for (index,data) in birthday_file.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"Day 32 - SMTP & DateTime/birthday-wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file = file_path) as letter_file:
        letter = letter_file.read()
        email_body = letter.replace(PLACEHOLDER, birthday_person["name"])

    with smtplib.SMTP(GMAIL_HOST) as connection:
        connection.starttls()
        connection.login(user = my_email, password = my_password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = birthday_person["email"],
            msg = f"Subject:Happy Birthday\n\n{email_body}"
            )
        print(f"Sent Birthday wishes to {birthday_person['name']}.")



# To get the python running in the cloud, Check pythonanywhere.com