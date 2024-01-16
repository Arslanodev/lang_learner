from typing import List

from mdpdf.converter import Converter
from markdownmaker.document import Document
from markdownmaker.markdownmaker import Header, Bold, Paragraph, Italic, OrderedList

from ..reverso_api.context import Translation, WordUsageExample


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


class Converter(Converter):
    def convert_md(self, md_text: str):
        ast = self.parser.parse(md_text)
        self.renderer.render(ast, "")


def __convert_data_to_md(data: List[tuple]) -> str:
    """Function converts structured data to md file

    arguments:
    - data     : Provide with data received from api
    - filename : name of md file that will be created
    """

    # Initializing Document class
    doc = Document()

    # Header of md file
    doc.add(Header(Bold("Translations")))

    # Parsing given data
    for translation, examples in data:
        # Adding translation of word
        doc.add(
            Paragraph(
                f'{Bold(translation.source_word)} - {", ".join(translation.translation)}'
            )
        )

        # Adding examples of word
        doc.add(
            OrderedList(
                tuple(
                    [
                        Italic(f"{example.source_text} - {example.target_text}")
                        for example in examples
                    ]
                )
            )
        )

    md_content = doc.write()

    return md_content


def convert_to_pdf(
    dataset: list[tuple[Translation, WordUsageExample]], outputFileName: str
) -> None:
    """Converts md text to pdf"""
    md_content = __convert_data_to_md(data=dataset)
    Converter(outputFileName).convert_md(md_content)
