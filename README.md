# Description
Open source python package that helps you to learn new words by creating pdf file containing translations and examples for each given word. The goal of this project is to make language learning fun and easy. Packge doesn't force you to learn but helps language learners to learn more effectively. No more online and offline courses. Learn for free and effectively. Give access to more people to learn language.

List of future funtionalities:
- ML to find most relevant words related to chosen field and level of fluency in language.
- Integration with ChatGPT for communicating using learned language
- Support for mp3 generation of words and sentences.
- There will be books translated into learned language or vice-versa. With dictionary of translations of each word.
- Support for teachers to whom you can ask questions and receive answers online. Like stackoverflow.
- Support for Quizes, Dashboards and Tests to make sure that you are progressing.


### Usage Example:
```python
"""Pdf generation"""
from lang_learner import Context

list_of_words = ["halo", "spiel", "verwenden"]

Context(words=list_of_words, target_lang="de", source_lang="en").create_pdf("translations.pdf")
```

```python
"""Voice translation mp3 generation"""
from lang_learner import Voice

Voice(
    source_txt="vorweisen", target_txt="to present", filename="speech_01"
).generate_speech()
```