from flask import Flask, request, send_file
from lang_learner.pdf_generator import convert_to_pdf
from lang_learner.context import ReversoContextAPI
from lang_learner.text_to_speech import Voice
import shutil
import os
import glob


app = Flask(__name__)


def delete_files():
    files = glob.glob("api/audio_files/*")
    for f in files:
        os.remove(f)


@app.post("/api/v1/pdf")
def generate_pdf():
    data = request.json
    obj = ReversoContextAPI(
        source_texts=data["source_texts"],
        source_lang=data["source_lang"],
        target_lang=data["target_lang"],
    ).get_data()

    convert_to_pdf(dataset=obj, outputFileName="api/pdf_files/trans.pdf")

    return send_file("pdf_files/trans.pdf", as_attachment=True)


@app.post("/api/v1/voice")
def generate_mp3():
    data = request.json
    obj = ReversoContextAPI(
        source_texts=data["source_texts"],
        source_lang=data["source_lang"],
        target_lang=data["target_lang"],
    ).get_data()

    for translation, _ in obj:
        Voice(
            source_txt=translation.source_word,
            target_txt=translation.translation[0],
            target_lang=data["target_lang"],
            source_lang=data["source_lang"],
            filename=f"api/audio_files/{translation.source_word}",
        ).generate_speech()

    shutil.make_archive(
        base_name="zip_files/audios",
        format="zip",
        root_dir="api",
        base_dir="audio_files",
    )
    delete_files()

    return {"download_link": "https://127.0.0.1:5000/api/v1/voice/audios.zip"}


@app.get("/api/v1/voice/<filename>")
def download_file(filename):
    return send_file(f"zip_files/{filename}", mimetype="application/zip")


@app.post("/api/v1/quiz")
def generate_quiz():
    pass


if __name__ == "__main__":
    app.run(debug=True)
