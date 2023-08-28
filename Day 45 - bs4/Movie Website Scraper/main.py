from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, 'html.parser')
title = soup.title.text.split("|")[0]
movies = []

movies_data = [movie.text for movie in soup.find_all(class_="listicleItem_listicle-item__title__hW_Kn")]
# print(movies_data)

# Reverse the order of the movies
movies_data.reverse()
# print(movies_data[::-1])

with open(file=f"{title}.txt", mode="w") as file:
    for movie in movies_data:
        file.write(f"{movie}\n")
