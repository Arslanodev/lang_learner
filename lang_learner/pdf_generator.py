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


def convert_data_to_md(data: List[tuple], filename: str) -> None:
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

    with open(f"{filename}.md", "w") as fl:
        fl.write(md_content)


def convert_md_to_pdf(pdf_filepath: str, md_filepath: str) -> None:
    """Function converts md file to pdf"""
    Converter(pdf_filepath).convert([md_filepath])


def generate_pdf(data: List[tuple], filepath: str) -> None:
    # Create md file
    # Convert md to pdf
    # delete md

    pass
