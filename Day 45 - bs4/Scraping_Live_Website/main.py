from bs4 import BeautifulSoup
import requests

# check 'website-link/robots.txt' to see instructions by the website for the users (crawlers)

response = requests.get(url = "https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

all_news = soup.find_all("span", class_="titleline")
all_texts = []
all_links = []
for news in all_news:
    news_text = news.find("a")
    text = news_text.text
    link = news_text.get("href")
    all_texts.append(text)
    all_links.append(link)

article_upvotes = [int(score.text.split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(all_texts)
print(all_links)
print(article_upvotes)
largest_number = max(article_upvotes)
highest_index = article_upvotes.index(largest_number)
print(highest_index)
print(all_texts[highest_index])
print(all_links[highest_index])
print(article_upvotes[highest_index])
