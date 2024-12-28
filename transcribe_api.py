import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.measure_time import measure_execution_time
import uvicorn
import requests

from services.audio_transcription_service import AudioTranscription
from services.video_transcription_service import Video2AudioConverter

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['*'], allow_methods=['*'])

output_path = './data'
n8n_webhook = "http://localhost:5678/webhook-test/8895e90e-a0d7-42b9-8aed-db2a21fe1e29"


class MessagePayload(BaseModel):
    url: str


def invoke_transcription(url):
    # download the audio from the url
    Video2AudioConverter().download_youtube_audio(url, output_path)

    # transcribe the audio into text
    is_audio_transcribed = AudioTranscription().transcribe(audio_file_dir=output_path, is_log_enabled=True)

    if is_audio_transcribed:
        return {'is_audio_transcribed': True}
    else:
        return {'is_audio_transcribed': False}


def invoke_n8n_workflow():
    # invoke n8n workflow using webhook
    requests.get(url=n8n_webhook)


@app.post("/api/v1/transcribe")
async def invoke_agents(payload: MessagePayload):

    @measure_execution_time
    async def process_transcription():
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(invoke_transcription, url=payload.url)]
            for future in as_completed(futures):
                result = future.result()
                if result["is_audio_transcribed"]:
                    invoke_n8n_workflow()

    # Schedule the transcription task to run asynchronously
    asyncio.create_task(process_transcription())

    # Respond immediately
    return {"is_transcription_started": True}


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000)
