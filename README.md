# Song Player

This Python script allows you to search for songs on YouTube or Spotify, select a song, and play it directly. It provides an interactive menu to choose a platform for searching and plays the song once selected.

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/OTAKUWeBer/AuraPlay
   cd AuraPlay
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Additionally, make sure to have **FFmpeg** and **yt-dlp** installed for audio handling and YouTube playback.

   - **Linux**: 
     - Install FFmpeg: `sudo apt install ffmpeg` (for Ubuntu/Debian-based systems) or `sudo pacman -S ffmpeg` (for Arch Linux).
     - Install yt-dlp: `sudo pip install yt-dlp`
   
   - **MacOS**:
     - Install FFmpeg: `brew install ffmpeg`
     - Install yt-dlp: `brew install yt-dlp`
   
   - **Windows**:
     - Download and install [FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.
     - Download [yt-dlp](https://github.com/yt-dlp/yt-dlp/releases) and place it in a directory in your system PATH.

## Usage

1. **Run the application:**
   ```bash
   python app.py
   ```

2. **Follow the prompts:**
   - Choose the platform (YouTube or Spotify).
   - Select the song you want to play.

## Spotify API Setup

To use the Spotify search and playback functionality, you need a Spotify API client ID and secret.

### Steps to Get Client ID and Secret

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click **Create an App** and enter the required details.
4. Once created, you’ll see your **Client ID** and **Client Secret** on the app dashboard.

### Environment Variable Setup

After obtaining the Client ID and Client Secret, create a `.env` file in the project directory to securely store your credentials:

```env
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

Replace `your_client_id` and `your_client_secret` with your actual Spotify credentials.

## Additional Notes

- **YouTube Playback**: The script uses `yt-dlp` to fetch and stream videos from YouTube. Ensure `yt-dlp` is installed and accessible in your system PATH.
- **Spotify Playback**: The script uses `spotipy` for Spotify API integration. 