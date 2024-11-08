import subprocess

def search_song_and_get_link():
    search = input('(YT) Enter the song name or "exit" to exit: ').strip()
    if search.lower() == 'exit':
        return None, None, None

    if not search:
        print("Invalid input. Please enter a song name or 'exit'.")
        return None, None, None

    # Run yt-dlp to search for the song and capture the output
    try:
        result = subprocess.run(
            ["yt-dlp", "--print", "title", "--print", "uploader", "--print", "format", "--get-url", "-f", "bestaudio", f"ytsearch:{search}"],
            capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running yt-dlp: {e}")
        return None, None, None

    # Check if the command was successful
    output = result.stdout.splitlines()
    if len(output) >= 4:
        song_name = output[0] if output[0] else "unknown"
        artist_name = output[1] if output[1] else "unknown"
        download_url = output[3]  # The download URL is the 4th line in the output
        return download_url, song_name, artist_name
    else:
        print("Error: Unexpected output format from yt-dlp.")
        return None, None, None

def play(download_url, song_name, artist_name):
    if not download_url or not song_name or not artist_name:
        print("Error: Missing song details. Cannot play the song.")
        return

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

def yt():
    while True:
        download_url, song_name, artist_name = search_song_and_get_link()
        if download_url and song_name and artist_name:
            play(download_url, song_name, artist_name)
        else:
            print("No valid song found or user exited.")
            break

if __name__ == "__main__":
    yt()
