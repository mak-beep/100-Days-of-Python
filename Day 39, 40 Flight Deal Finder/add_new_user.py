# This file is for adding new users to the email list.
import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_USER_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")

FirstName = input("What is your First Name? ")
LastName = input("What is your Last Name? ")
email1 = "email1"
email2 = "email2"
while email1 != email2:
    email1 = input("What is your Email? ").lower()
    if (email1 == "exit" or email1 == "quit"):
        exit()
    email2 = input("Please verify your Email? ").lower()
    if (email2 == "exit" or email2 == "quit"):
        exit()

new_user = {
    'user': {
        'firstName': FirstName,
        'lastName': LastName,
        'email': email1
    }
}

response = requests.post(url=SHEETY_USER_ENDPOINT, json=new_user)
response.raise_for_status()
# print(response.text)
print(f"{FirstName}, You have been added to the list.")