# Project Description
Services that helps to learn languages. Currently there are two services. First is dictionary generator. Second service generates mp3 dictations of each given word. 


## Service dictionary Generator
Service for generating pdf file containing translations and examples of given list of words

### API endpoints
`POST` - `/api/v1/pdf`. Request data:
```json
{
    "source_texts": ["hello", "world"],
    "source_lang": "en",
    "target_lang": "de"
}
```
As a response:
```json
{
    "download_link": "http://localhost:8000/<filename>.pdf"
}
```

## Service Spoken Words
Service for generating mp3 files containing spoken words with translations

### API endpoints

`POST` - `api/v1/voice`. Request data should contain:
```json
{
    "source_texts": ["hello", "world"],
    "source_lang": "en",
    "target_lang": "de"
}
```

As a response:
```json
{
    "download_link": "http://localhost:8080/<filename>.zip"
}
```

**Future list of features:**  
    - API gateway setup  
    - API key authendication  
    - Telegram bot integration  
    - Asynchronous code implementation  


# How to run this application
1. Simply clone this project on you local computer with command:  
```bash
git clone https://github.com/Arslanodev/lang_learner.git
```
2. Go into the project folder through terminal command:  
```bash
cd lang_learner
```

3. Install docker on your machine and simply run this command:
```bash
docker-compose up
```
Open ports are:
- dictionary generator == `8000`
- voice generator == `8080`

You can change ports mapping inside `docker-compose.yml`

This project is still under development. So there might be some issues with language support and others.