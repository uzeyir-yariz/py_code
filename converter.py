from moviepy.editor import *
import os

def convert_to_mp3(file_path):
    try:
        # Get the name of the file without the extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]

        # Load the video file
        video = VideoFileClip(file_path)

        # Convert the video to audio
        audio = video.audio

        # Save the audio as an mp3 file
        audio.write_audiofile(os.path.join('mp3', f'{file_name}.mp3'))
    except KeyError as e:
        print(f"An error occurred: {e}")
        print("This might be due to an invalid or unsupported video file. Please ensure that the video file is valid and in a supported format.")

def main():
    # Make sure the 'mp3' folder exists
    if not os.path.exists('mp3'):
        os.makedirs('mp3')

    # Get the list of all files in the 'mp4' folder
    files = os.listdir('mp4')

    # Filter out only the mp4 files
    mp4_files = [file for file in files if file.endswith('.mp4')]

    # Convert each MP4 file to MP3
    for mp4_file in mp4_files:
        mp4_path = os.path.join('mp4', mp4_file)
        convert_to_mp3(mp4_path)

if __name__ == "__main__":
    main()
