# Project Description
Services that helps to learn languages. Currently there are two services. First is dictionary generator. Second service generates mp3 dictations of each given word. 

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
As a response:
```json
{
    "download_link": "http://localhost:8000/alsdjfwer1e12.pdf"
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

As a response:
{
    "download_link": "http://localhost:8000/asdjlsdfkj1wqe.zip
}

The project is still in development. So there might be some issues.
