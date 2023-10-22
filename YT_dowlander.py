from pytube import Playlist
import os

# YouTube çalma listesi URL'sini belirtin
playlist = Playlist("youtube_playlist_url")

# MP4 klasörünü oluşturun (eğer yoksa)
mp4_folder = 'mp4'
os.makedirs(mp4_folder, exist_ok=True)

print("videos count : ", len(playlist.video_urls))

for video in playlist.videos:
    video_stream = video.streams.filter(only_audio=True).first()
    video_stream.download(output_path=mp4_folder)
