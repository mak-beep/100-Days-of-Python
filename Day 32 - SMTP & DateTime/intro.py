import smtplib

my_email = "danishtaimoor21@gmail.com"
my_password = "12345678@90"

GMAIL_HOST = "smtp.gmail.com"
HOTMAIL_HOST = "smtp.live.com"
YAHOO_HOST = "smtp.mail.yahoo.com"

# Starting the connection 
# connection = smtplib.SMTP(GMAIL_HOST)
with smtplib.SMTP(GMAIL_HOST) as connection:

    # starttls() stands for transport layer security - securing connection to email server
    connection.starttls()

    # To login
    connection.login(user=my_email, password= my_password)

    # Send Email
    # msg = "Subject: subject \n\n body of email"
    connection.sendmail(from_addr=my_email, to_addrs="test_email@gmail.com", msg="Subject: Greetings\n\nHello")

# Close Connection - or we can use the 'with' command
# connection.close()


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
if month == 8:
    print("This month.")

day_of_week = now.weekday()
print(day_of_week)

# Fix time
date_of_birth = dt.datetime(year=2001, month = 11, day=7)
print(date_of_birth)
