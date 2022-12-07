from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


date = "2022-09-30"#input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_endpoint = f"https://www.billboard.com/charts/hot-100/{date}"


response = requests.get(billboard_endpoint)
soup = BeautifulSoup(response.text, "html.parser")


all_rows = soup.find_all(name="li", class_="o-chart-results-list__item")
all_titles = [row.h3.getText().strip() for row in all_rows if row.h3 != None]
all_artists = [row.span.getText().strip() for row in all_rows if row.h3 != None]

song_uris = []


for title in all_titles:
    index = all_titles.index(title)
    songresult = sp.search(f"track:{title} artist:{all_artists[index]}", type="track",limit = 2)
    try:
        uri = songresult["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")
        
playlist = sp.user_playlist_create(SPOTIFY_ID,f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)