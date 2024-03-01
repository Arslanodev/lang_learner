import uuid
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from reverso_api import ReversoContextAPI

from .schemas import Data
from .pdf_generator import convert_to_pdf

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


@app.get("/api/v1/download/{filename}")
def download_file(filename):
    filepath = Path(f"file_storage/{filename}")

    return FileResponse(filepath, media_type="application/octet-stream")
