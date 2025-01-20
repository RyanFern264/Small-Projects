from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"

#spotify authenticator using my env vars
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#made a function so that I can call it back in case the date fails
def create_playlist():
    time_period = input("What year do you want to travel to? Type the date in the format:YYYY-MM-DD\n")

    url = f"https://www.billboard.com/charts/hot-100/{time_period}"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

    request = requests.get(url=url, headers=header)
    top_100_page = request.text

    soup = BeautifulSoup(top_100_page, "html.parser")
    song_titles_spans = soup.select("li ul li h3") #getting song names
    song_names = [song.getText().strip() for song in song_titles_spans]

    #if song names actually populated, seems like sometimes it doesn't randomly depending on date?
    if song_names:
        track_uris = []

        #searching for song URIs based on the name
        for song in song_names:
            search_results = sp.search(q=song, limit=1, type="track")
            track_uris.append(search_results['tracks']['items'][0]['uri'])

        playlist = sp.user_playlist_create(
            user=sp.current_user()["id"],
            name=f"{time_period}_top_100",
            public=False,
            description="Top 100 songs for the specified time period beep boop")

        playlist_id = playlist["id"]
        print(playlist_id)

        #populate the playlist with the songs provided
        try:
            sp.playlist_add_items(playlist_id, track_uris)
            print("Track(s) added successfully!")
        except spotipy.exceptions.SpotifyException as e:
            print(f"An error occurred: {e}")
    else:
        print("idk that date didn't work try again dude")
        create_playlist()

create_playlist()