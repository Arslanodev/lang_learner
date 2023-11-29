# Description
Python package that helps in learning new words by creating pdf file containing translations and examples for each given word.

### Usage Example:
```python
from lang_learner import Context

list_of_words = ["halo", "spiel", "verwenden"]

Context(words=list_of_words, target_lang="de", source_lang="en").create_pdf("translations.pdf")
```
