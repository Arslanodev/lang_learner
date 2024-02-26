import uuid
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from reverso_api import ReversoContextAPI

from schemas import Data
from lang_learner.pdf_generator import convert_to_pdf
from lang_learner.speech_generator import generate_mp3

app = FastAPI()

Path("file_storage").mkdir(exist_ok=True, parents=True)


@app.post("/api/v1/pdf")
def generate_pdf(data: Data):
    obj = ReversoContextAPI(
        source_texts=data.source_texts,
        source_lang=data.source_lang,
        target_lang=data.target_lang,
    ).get_data()

    filename = uuid.uuid4()
    filepath = f"file_storage/{filename}.pdf"
    convert_to_pdf(dataset=obj, outputFileName=filepath)

    return {"download_link": f"/api/v1/download/{filename}.pdf"}


@app.post("/api/v1/voice")
def mp3_generator(data: Data):
    filename = generate_mp3(
        source_texts=data.source_texts,
        source_lang=data.source_lang,
        target_lang=data.target_lang,
    )

    return {"download_link": f"/api/v1/download/{filename}.zip"}


@app.post("/api/v1/quiz")
def quiz_generator():
    return {"message": "Not implemented yet"}


@app.get("/api/v1/download/{filename}")
def download_file(filename):
    filepath = Path(f"file_storage/{filename}")

    return FileResponse(filepath, media_type="application/octet-stream")


if __name__ == "__main__":
    uvicorn.run(app)
