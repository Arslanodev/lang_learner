from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


client = TestClient(app)

data = {
    "source_texts": ["hello", "world"],
    "source_lang": "en",
    "target_lang": "de",
}


def test_pdf_gen():
    response = client.post(url="/api/v1/pdf", data=data)

    assert response.status_code == 200
    assert response.json() == {"download_link": ""}


def test_voice_gen():
    response = client.post(url="/api/v1/pdf", data=data)

    assert response.status_code == 200
    assert response.json() == {"download_link": ""}
