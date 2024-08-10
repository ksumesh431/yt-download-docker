# YouTube Audio Downloader

This repository contains a Python script and a Dockerfile to download audio from YouTube videos and playlists. The script uses `yt-dlp` to extract audio and save it in MP3 format. The Dockerfile sets up an environment to run the script in a container.

## Python Script

### Description

The `script.py` file allows you to download audio from a YouTube video or playlist. The downloaded audio is converted to MP3 format and saved with a high bitrate of 320 kbps.

### Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Install dependencies:**

    Ensure you have Python 3.9 and `yt-dlp` installed. You can install `yt-dlp` via pip:

    ```bash
    pip install yt-dlp
    ```

3. **Run the script:**

    To download audio from a single video:

    ```bash
    python script.py <youtube_video_url>
    ```

    To download audio from a playlist:

    ```bash
    python script.py <youtube_playlist_url>
    ```

    Replace `<youtube_video_url>` or `<youtube_playlist_url>` with the actual URL of the YouTube video or playlist.

## Dockerfile

### Description

The Dockerfile creates a Docker image that contains Python, `ffmpeg`, and `yt-dlp`. It sets up an environment to run the audio downloading script in a container.

### Building the Docker Image

1. **Build the Docker image:**

    ```bash
    docker build -t youtube-audio-downloader .
    ```

2. **Run the Docker container:**

    To download audio from a single video:

    ```bash
    docker run --rm -v $(pwd)/data:/data youtube-audio-downloader <youtube_video_url>
    ```

    To download audio from a playlist:

    ```bash
    docker run --rm -v $(pwd)/data:/data youtube-audio-downloader <youtube_playlist_url>
    ```

    Replace `<youtube_video_url>` or `<youtube_playlist_url>` with the actual URL of the YouTube video or playlist. The `-v $(pwd)/data:/data` flag mounts the local `data` directory to the container’s `/data` directory to store the downloaded files.

### Directory Structure

- `script.py`: The Python script for downloading audio.
- `Dockerfile`: The Dockerfile to build the Docker image.



