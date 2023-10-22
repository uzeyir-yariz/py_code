import os
from moviepy.editor import VideoFileClip

mp4_folder = 'mp4'  # MP4 dosyalarının bulunduğu klasör
mp3_folder = 'mp3'  # Dönüştürülen MP3 dosyalarının kaydedileceği klasör

os.makedirs(mp3_folder, exist_ok=True)  # MP3 klasörünü oluştur (eğer yoksa)

for mp4_filename in os.listdir(mp4_folder):
    if mp4_filename.endswith('.mp4'):
        mp4_path = os.path.join(mp4_folder, mp4_filename)
        mp3_filename = mp4_filename.split('.')[0] + '.mp3'
        mp3_path = os.path.join(mp3_folder, mp3_filename)

        video_clip = VideoFileClip(mp4_path)

        # Sadece sesi çıkart ve MP3 dosyasını kaydet
        audio_clip = video_clip.audio
        audio_clip.fps = 24
        audio_clip.write_audiofile(mp3_path)

print("Dönüştürme işlemi tamamlandı.")
