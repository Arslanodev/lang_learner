from flask import Flask, request, send_file
from pdf_generator import convert_to_pdf

app = Flask(__name__)


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
