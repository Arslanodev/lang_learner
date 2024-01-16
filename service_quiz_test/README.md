# Service Quiz Test
Service for generating quiz tests in a pdf format with anwer keys on the end of the page.

### API endpoints
`POST` - `api/v1/quiz`. Request data:
```json
{
    "words": ["word", "word_1"],
    "source_lang": "en",
    "target_lang": "de"
}
```

`RESPONSE` --> pdf file