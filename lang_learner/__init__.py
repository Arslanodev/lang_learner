from typing import List

from lang_learner.pdf_generator import convert_to_pdf
from lang_learner.context import ReversoContextAPI


class Context:
    """Generates pdf file containing translations and examples of given words"""

    def __init__(self, source_lang="de", target_lang="en", words=["vorweisen"]):
        self.target_lang = target_lang
        self.source_lang = source_lang
        self.words = words

    def create_pdf(self, filepath: str) -> None:
        data = ReversoContextAPI(
            source_texts=self.words,
            source_lang=self.source_lang,
            target_lang=self.target_lang,
        ).get_data()

        convert_to_pdf(dataset=data, outputFileName=filepath)
