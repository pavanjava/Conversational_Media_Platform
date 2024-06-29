import whisper
from pathlib import Path
import os

# Define the directory and file path
dir_path = './transcriptions'


class AudioTranscription:
    def __init__(self):
        self.model = whisper.load_model("small")

    def transcribe(self, audio_file_dir: str = '', is_log_enabled: bool = False) -> bool:
        for file_path in Path(audio_file_dir).rglob('*'):
            if file_path.is_file():
                if is_log_enabled:
                    print(file_path)
                try:
                    result = self.model.transcribe(audio=f'./{file_path}', word_timestamps=True)
                    if is_log_enabled:
                        print(result)

                    # Ensure the directory exists
                    os.makedirs(dir_path, exist_ok=True)

                    with open(file=f'{dir_path}/{file_path.name}_transcript.txt', mode='w') as transcription:
                        transcription.write(result.get('text'))
                except Exception as e:
                    print('Error', e.__cause__)
                    return False
        return True
