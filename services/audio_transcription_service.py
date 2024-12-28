import whisper
from pathlib import Path
from utils.measure_time import measure_execution_time
import os
import logging

# Define the directory and file path
dir_path = './transcriptions'


class AudioTranscription:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)  # Set logging level
        self.logger.info("Loading Whisper model")  # Log model loading
        self.logger.info(whisper.available_models())
        self.model = whisper.load_model("medium")

    @measure_execution_time
    def transcribe(self, audio_file_dir: str = '', is_log_enabled: bool = False) -> bool:

        for file_path in Path(audio_file_dir).rglob('*'):
            if file_path.is_file():
                if is_log_enabled:
                    self.logger.info(f"audio file path: {file_path} ")
                try:
                    result = self.model.transcribe(audio=f'./{file_path}', word_timestamps=True)
                    if is_log_enabled:
                        self.logger.info(result)

                    # Ensure the directory exists
                    self.logger.info("creating the directory if it does not exist")
                    os.makedirs(dir_path, exist_ok=True)

                    with open(file=f'{dir_path}/{file_path.name}_transcript.txt', mode='w') as transcription:
                        transcription.write(result.get('text'))

                    if is_log_enabled:
                        self.logger.info(f"transcription completed successfully for file: {file_path.name} "
                                         f"in directory: {dir_path}")

                except Exception as e:
                    self.logger.error('Error', e.__cause__)
                    return False
        return True
