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
stock_data = stock_response.json()
stock_info = stock_data["Time Series (Daily)"]
# print(Stock_info)
recent_stocks = []
for day in stock_info:
    recent_stocks.append(float(stock_info[day]["4. close"]))
    if len(recent_stocks)==2:
        break
# print(Recent_stocks)
change = round(((recent_stocks[0] - recent_stocks[1])/recent_stocks[1]) * 100,2)
if (change>0):
    effect = f"🔺{abs(change)}%"
else:
    effect = f"🔻{abs(change)}%"
# print(change)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_parameters = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": os.environ.get("NEWS_API_KEY")
}
news_response = requests.get(url= NEWS_ENDPOINT, params=news_parameters)
# news_response.raise_for_status()
latest_news = []
news_data = news_response.json()["articles"]
for news in news_data:
    i = len(latest_news)
    headline = news["title"]
    brief = news["description"]
    new_news = {}
    new_news["headline"] = headline
    new_news["brief"] = brief
    latest_news.append(new_news)
    if len(latest_news) == 3:
        break

# print(latest_news)
# print(news_data)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# print(f"{STOCK}: {effect}\nHeadline: {latest_news[0]['headline']}\nBrief: {latest_news[0]['description']}\nHeadline: {latest_news[0]['headline']}\nBrief: {latest_news[0]['description']}\nHeadline: {latest_news[0]['headline']}\nBrief: {latest_news[0]['description']}")
client = Client(account_sid, auth_token)
# print({latest_news[0]})
message = client.messages \
    .create(
    body=f'''
    {STOCK}: {effect}
    Headline: {latest_news[0]['headline']}
    Brief: {latest_news[0]['brief']}
    Headline: {latest_news[1]['headline']}
    Brief: {latest_news[1]['brief']}
    Headline: {latest_news[2]['headline']}
    Brief: {latest_news[2]['brief']}
    ''',
    from_= os.environ.get("from_phone"),
    to = os.environ.get("to_phone")
)
print(message.body)
#
print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

