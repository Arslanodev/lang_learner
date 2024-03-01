from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from .schemas import Data
from .speech_generator import generate_mp3

app = FastAPI()

Path("file_storage").mkdir(exist_ok=True, parents=True)


@app.post("/api/v1/voice")
def mp3_generator(data: Data):
    filename = generate_mp3(
        source_texts=data.source_texts,
        source_lang=data.source_lang,
        target_lang=data.target_lang,
    )

    return {"download_link": f"/api/v1/download/{filename}.zip"}


@app.get("/api/v1/download/{filename}")
def download_file(filename):
    filepath = Path(f"file_storage/{filename}")

    return FileResponse(filepath, media_type="application/octet-stream")
