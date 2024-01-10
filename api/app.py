from flask import Flask, request, send_file
from lang_learner.pdf_generator import convert_to_pdf
from lang_learner.context import ReversoContextAPI

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


@app.post("/api/v1/voice")
def generate_mp3():
    pass


@app.post("/api/v1/quiz")
def generate_quiz():
    pass


if __name__ == "__main__":
    app.run(debug=True)
