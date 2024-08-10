import sys
import yt_dlp

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': '/data/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Downloaded audio from {url}")
    except Exception as e:
        print(f"Failed to download audio: {e}")

def download_playlist_audio(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': '/data/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
            print(f"Downloaded playlist from {playlist_url}")
    except Exception as e:
        print(f"Failed to download playlist: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <youtube_link_or_playlist>")
        sys.exit(1)

    url = sys.argv[1]
    if "playlist" in url:
        print("Downloading playlist...")
        download_playlist_audio(url)
    else:
        print("Downloading single video...")
        download_audio(url)

    print("Download completed.")
    return

if __name__ == "__main__":
    main()
