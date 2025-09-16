import requests
import spotipy
import os
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv('CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('REDIRECT_URI')
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET, 
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))    

user_id = sp.current_user()['id'] # type: ignore

date_prompt = input("Enter a date in the format YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/" + date_prompt

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

response = requests.get(URL, headers = header)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

# find song title by id = "title-of-a-story"
song_titles = soup.select("ul li ul li h3")
song_names = []
for song in song_titles:
    song_names.append(song.getText().strip())

# print(song_names)

# find song uri
song_uris = []
year = date_prompt.split("-")[0]
for song in song_names:
    result = sp.search(q = f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result['tracks']['items'][0]['uri'] # type: ignore
        song_uris.append(uri)
    except IndexError:
        print("No song found --> Skipped")


# creating spotify playlist using song names

playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Hot 100 - {date_prompt}", description=f"Billboard Hot 100 - {date_prompt}", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris) # type: ignore

print("Playlist created successfully")