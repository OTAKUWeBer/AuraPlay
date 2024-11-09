import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import subprocess
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set your Spotify client ID and client secret as environment variables for security.
SPOTIPY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

def check_spotipy_credential():
    # Ensure that credentials are available
    if not SPOTIPY_CLIENT_ID or not SPOTIPY_CLIENT_SECRET:
        print("Error: Spotify client ID and secret are required.")
        exit()

def authenticate_spotify():
    # Authenticate using client credentials
    auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
    return spotipy.Spotify(auth_manager=auth_manager)

def search_song_and_get_link(sp):
    while True:  # Loop to ask for a song after one completes
        song_name = input("(Spotify) Enter the song name (or type 'exit' to quit): ")

        if song_name.lower() == 'exit':
            print("Exiting the program.")
            break

        try:
            # Search for the song
            results = sp.search(q=song_name, limit=1, type='track')
            if results['tracks']['items']:
                track = results['tracks']['items'][0]
                song_url = track['external_urls']['spotify']
                song_id = song_url.split("/")[-1]
                song_name = track['name']
                artist_name = track['artists'][0]['name']
                print(f"Spotify search successful")
                get_gid(song_id, song_name, artist_name)
            else:
                print("Song not found.")
        except Exception as e:
            print(f"An error occurred while searching for the song: {e}")

def get_gid(song_id, song_name, artist_name):
    url = f"https://api.fabdl.com/spotify/get?url=https://open.spotify.com/track/{song_id}"

    try:
        # Make the GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the JSON data
        data = response.json()
        track_id = data['result']['id']
        gid = data['result']['gid']
        get_download_link(gid, track_id, song_name, artist_name)
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data for the song: {e}")

def get_download_link(gid, track_id, song_name, artist_name):
    url = f"https://api.fabdl.com/spotify/mp3-convert-task/{gid}/{track_id}"

    try:
        # Make the GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the JSON data
        data = response.json()
        # Get the download link
        download_url = data['result']['download_url']
        play(download_url, song_name, artist_name)
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve download link: {e}")

def play(download_url, song_name, artist_name):
    download_url = f"https://api.fabdl.com{download_url}/"
    print(f"Now playing: {song_name} by {artist_name}")
    
    try:
        # Run ffplay and suppress all the output
        subprocess.run(
            ["ffplay", "-nodisp", "-autoexit", "-vn", download_url],
            check=True,
            stdout=subprocess.DEVNULL,  # Suppress standard output
            stderr=subprocess.DEVNULL   # Suppress error output
        )
        print(f"Finished playing: {song_name} by {artist_name}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while playing the song: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while playing the song: {e}")

def spotify():
    check_spotipy_credential()  # Check credentials before proceeding
    sp = authenticate_spotify()  # Authenticate Spotify client
    search_song_and_get_link(sp)  # Start the search and play process

if __name__ == "__main__":
    spotify()
