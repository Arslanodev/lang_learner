# Service Dict Generator
Service for generating pdf file containing translations and examples of given words

### API endpoints
`POST` - `/api/v1/pdf`. Request data:
```json
{
    "source_texts": ["hello", "world", "bro"],
    "source_lang": "en",
    "target_lang": "de"
}
```


# Service Spoken Words
Service for generating mp3 files containing spoken words with translations

### API endpoints

`POST` - `api/v1/voice`. Request data should contain:
```json
{
    "source_texts": ["hello", "world", "bro"],
    "source_lang": "en",
    "target_lang": "de"
}
```

`RESPONSE` --> download link for zip file containing mp3 files

The project is still in development. So there might be some issues.