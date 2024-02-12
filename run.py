import uuid

from flask import Flask, request, send_file
from reverso_api import ReversoContextAPI

from module.pdf_generator import convert_to_pdf
from module.speech_generator import generate_mp3

app = Flask(__name__)


@app.post("/api/v1/pdf")
def generate_pdf():
    data = request.json
    obj = ReversoContextAPI(
        source_texts=data["source_texts"],
        source_lang=data["source_lang"],
        target_lang=data["target_lang"],
    ).get_data()

    filename = uuid.uuid4()
    filepath = f"file_storage/{filename}.pdf"
    convert_to_pdf(dataset=obj, outputFileName=filepath)

    return {
        "download_link": f"/api/v1/download/{filename}"
    }


@app.post("/api/v1/voice")
def mp3_generator():
    data = request.json
    filename = generate_mp3(source_texts=data["source_texts"], source_lang=data["source_lang"],
                            target_lang=data["target_lang"])

    return {
        "download_link": f"/api/v1/download/{filename}"
    }


@app.post("/api/v1/quiz")
def quiz_generator():
    return {
        "message": "Not implemented yet"
    }


@app.get("/api/v1/download/<filename>")
def download_file(filename):
    filepath = f"file_storage/{filename}"

    return send_file(filepath, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)
