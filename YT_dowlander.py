import os
from pytube import Playlist

def download_playlist(url, output_folder):
    try:
        playlist = Playlist(url)

        # Oluşturulan çalma listesindeki her bir videoyu indir
        for video in playlist.videos:
            video.streams.get_highest_resolution().download(output_path=output_folder)

        print("Çalma listesi indirme tamamlandı.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    user_url = input("YT list URL")
    playlist_url = user_url  # İndirmek istediğiniz çalma listesinin URL'sini buraya ekleyin
    output_folder = "mp4"  # İndirilen videoların kaydedileceği klasörü burada belirtin

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    download_playlist(playlist_url, output_folder)
