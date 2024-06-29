from pytube import YouTube
import moviepy.editor as mp
import os


class Video2AudioConverter:

    def download_youtube_audio(self, youtube_url, output_path):
        # temp audio file name
        temp_audio_file = 'temp_audio.mp4'

        # Create a YouTube object
        yt = YouTube(youtube_url)

        # Select the best audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream to a temporary file
        audio_stream.download(filename=temp_audio_file)

        # Convert the downloaded file to MP3
        clip = mp.AudioFileClip(temp_audio_file)
        clip.write_audiofile(output_path)

        # Remove the temporary MP4 file
        clip.close()
        # Check if the file exists before attempting to delete it
        if os.path.exists(temp_audio_file):
            os.remove(temp_audio_file)
            print(f"{temp_audio_file} has been deleted successfully.")
        else:
            print(f"{temp_audio_file} does not exist in the current directory or its already deleted")
