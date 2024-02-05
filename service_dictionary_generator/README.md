# Service Dict Generator
Service for generating pdf file containing translations and examples of given words

### API endpoints
`POST` - `/api/v1/pdf`. Request data:
```json
{
    "source_texts": ["word_1", "word_2", "word_3"],
    "source_lang": "en",
    "target_lang": "de"
}
```