from twilio.rest import Client
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

TWILIO_SID = os.environ.get("account_sid")
TWILIO_AUTH_TOKEN = os.environ.get("auth_token")
TWILIO_FROM_NUMBER = os.environ.get("from_phone")
TWILIO_TO_NUMBER = os.environ.get("to_phone")
EMAIL_PROVIDER_SMTP_ADDRESS = os.environ.get("EMAIL_PROVIDER_SMTP_ADDRESS")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


class NotificationManager:

    # Initializing the connection
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Sending SMS with Flight details
    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_FROM_NUMBER,
            to=TWILIO_TO_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
