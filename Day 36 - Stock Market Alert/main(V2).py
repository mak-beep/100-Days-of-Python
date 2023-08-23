import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("STOCK_API_KEY")
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_info = [value for (key,value) in stock_data.items()]

yesterday_closing_price = stock_info[0]["4. close"]
day_before_yesterday_closing_price = stock_info[1]["4. close"]
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
diff_percentage = round((difference / float(yesterday_closing_price)) * 100,2)
if (diff_percentage>0):
    stock_activity = f"🔺{abs(diff_percentage)}%"
else:
    stock_activity = f"🔻{abs(diff_percentage)}%"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_parameters = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": os.environ.get("NEWS_API_KEY")
}
news_response = requests.get(url= NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()["articles"]
latest_news = news_data[:3]

formatted_news = [f"{STOCK}: {stock_activity}\nHeadline:{article['title']}.\nBrief:{article['description']}" for article in latest_news]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

client = Client(account_sid, auth_token)
for article in formatted_news:
    message = client.messages \
        .create(
        body=article,
        from_= os.environ.get("from_phone"),
        to = os.environ.get("to_phone")
    )
    print(message.body)
    print(message.status)

