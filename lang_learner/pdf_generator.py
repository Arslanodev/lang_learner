from typing import List

from mdpdf.converter import Converter
from markdownmaker.document import Document
from markdownmaker.markdownmaker import (
    Header,
    Bold,
    Paragraph,
    Italic,
    OrderedList
)


class Converter(Converter):
    def convert_md(self, md_text: str):
        ast = self.parser.parse(md_text)
        self.renderer.render(ast, "")


def convert_data_to_md(data: List[tuple]) -> str:
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
            Paragraph(f'{Bold(translation.source_word)} - {", ".join(translation.translation)}'))

        # Adding examples of word
        doc.add(OrderedList(
            tuple([
                Italic(f"{example.source_text} - {example.target_text}")
                for example in examples
            ])
        ))

    md_content = doc.write()

    return md_content


def create_pdf(dataset: List[tuple], outputFileName: str) -> None:
    """Converts md text to pdf"""
    md_content = convert_data_to_md(data=dataset)
    Converter(outputFileName).convert_md(md_content)
