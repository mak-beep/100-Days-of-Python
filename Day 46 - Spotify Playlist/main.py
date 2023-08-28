import requests
from bs4 import BeautifulSoup
import spotipy
import os
from dotenv import load_dotenv

load_dotenv()

from spotipy.oauth2 import SpotifyOAuth

# Spotify Guide - Documentation
# https://spotipy.readthedocs.io/en/2.22.1/#getting-started

# Scope of the app
scope = "playlist-modify-private"
# Spotify Object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope= scope, client_id=os.environ.get("SPOTIPY_CLIENT_ID"), client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"), redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"), show_dialog=True, cache_path="token.txt"))
# User ID
user_id = sp.current_user()["id"]
# print(user_id)

# Basic Link to scrap
URL = "https://www.billboard.com/charts/hot-100/"
# Date user is interested in
date = input("Which year do you want to travel to? (YYYY-MM-DD) ")
# Splitting year
year = date.split("-")[0]

response = requests.get(url=URL+date)
html_data = response.text

soup = BeautifulSoup(html_data, 'html.parser')
# Getting hold of track elements
songs = soup.select('li ul li h3')
# Storing names
tracks = [song.text.strip() for song in songs]
# print(tracks)
# print(len(tracks))

# For storing URIs
song_uris = []

# Create a playlist
playlist_ = sp.user_playlist_create(user=user_id, name=date, public=False)
# Get the playlist id
playlist_id = playlist_["id"]

# generating URI for each track in the list
for track in tracks:
    # Searching the song by its name and year
    result = sp.search(q=f"track:{track} year:{year}", type="track")
    # print(result)
    try:
        # Getting hold of the track's URI
        uri = result["tracks"]["items"][0]["uri"]
        # Add to the list
        song_uris.append(uri)
    except IndexError:
        print(f"{track} doesn't exist in Spotify. Skipped.")

# Songs URIs
print(song_uris)
# Adding to the playlist created above
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

