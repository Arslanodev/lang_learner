import uuid

from flask import Flask, request, send_file
from reverso_api import ReversoContextAPI

from module.pdf_generator import convert_to_pdf

app = Flask(__name__)


@app.post("/api/v1/pdf")
def generate_pdf():
    data = request.json
    obj = ReversoContextAPI(
        source_texts=data["source_texts"],
        source_lang=data["source_lang"],
        target_lang=data["target_lang"],
    ).get_data()

    filepath = f"file_storage/{uuid.uuid4()}.pdf"
    convert_to_pdf(dataset=obj, outputFileName=filepath)

    return send_file(filepath, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)
