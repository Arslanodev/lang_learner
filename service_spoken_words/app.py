import os
import pathlib
import shutil
import tempfile
import uuid

from flask import Flask, request, send_file
from reverso_api import ReversoContextAPI

from text_to_speech import Voice

app = Flask(__name__)
pathlib.Path("file_storage").mkdir(parents=True, exist_ok=True)
pathlib.Path("temp_dirs").mkdir(parents=True, exist_ok=True)


@app.post("/api/v1/voice")
def generate_mp3():
    temp_dir = tempfile.TemporaryDirectory(dir="./temp_dirs")
    dir_name = temp_dir.name.split("/")[-1]
    zip_dir_name = "voices"

    os.makedirs(os.path.join(temp_dir.name, zip_dir_name))

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
            filename=os.path.join(temp_dir.name, zip_dir_name, translation.source_word),
        ).generate_speech()

    unique_filename = str(uuid.uuid4())
    shutil.make_archive(
        base_name=f"file_storage/{unique_filename}",
        format="zip",
        root_dir=f"temp_dirs/{dir_name}",
        base_dir="voices",
    )
    temp_dir.cleanup()
    # Delete files

    return {"download_link": f"http://127.0.0.1:8000/api/v1/voice/{unique_filename}"}


@app.get("/api/v1/voice/<filename>")
def download_file(filename):
    return send_file(
        f"file_storage/{filename}.zip", mimetype="application/zip", as_attachment=True
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)
