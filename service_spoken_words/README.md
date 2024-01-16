# Service Spoken Words
Service for generating mp3 files containing spoken words with translations

### API endpoints

`POST` - `api/v1/speak`. Request data should contain:
```json
"data": {
    "words": {
        "word_1": "word_1",
        "word_2": "word_2"
    }
    "source_lang": "en",
    "target_lang": "de"
}
```

`RESPONSE` --> download link for zip file containing mp3 files