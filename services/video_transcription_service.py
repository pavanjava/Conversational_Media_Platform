from pytubefix import YouTube
from moviepy.editor import AudioFileClip
from utils.measure_time import measure_execution_time
import os
import logging


class Video2AudioConverter:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)  # Set logging level

    @measure_execution_time
    def download_youtube_audio(self, youtube_url, output_path):

        self.logger.info(f"Downloading audio from YouTube URL: {youtube_url}")
        # temp audio file name
        temp_audio_file = 'temp_audio.mp4'

        # Create a YouTube object
        yt = YouTube(youtube_url, use_oauth=False, allow_oauth_cache=True)

        # Select the best audio stream
        audio_stream = yt.streams.get_audio_only()

        # Download the audio stream to a temporary file
        audio_stream.download(filename=temp_audio_file)

        # Get the audio track name for naming the output file
        audio_name = "output.mp3"

        # Convert the downloaded file to MP3
        self.logger.info(f"Converting audio to MP3 and saving at: {output_path}/{audio_name}")
        clip = AudioFileClip(temp_audio_file)
        clip.write_audiofile(output_path+f"/{audio_name}")

        # Remove the temporary MP4 file
        self.logger.info("Removing temporary MP4 file.")
        clip.close()
        # Check if the file exists before attempting to delete it
        if os.path.exists(temp_audio_file):
            os.remove(temp_audio_file)
            print(f"{temp_audio_file} has been deleted successfully.")
        else:
            print(f"{temp_audio_file} does not exist in the current directory or its already deleted")
