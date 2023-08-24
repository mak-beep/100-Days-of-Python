import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
SHEET_PRICES_ENDPOINT = os.environ.get("SHEET_PRICES_ENDPOINT")
SHEET_USERS_ENDPOINT = os.environ.get("SHEET_USERS_ENDPOINT")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_PRICES_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_code(self):
        # Checking for missing 'iataCode'
        for city in self.destination_data:
            id = city["id"]
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_PRICES_ENDPOINT}/{id}", json=new_data)
            response.raise_for_status()
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
