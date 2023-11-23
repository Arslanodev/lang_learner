import requests

from markdowngenerator import MarkdownGenerator
from mdpdf.converter import Converter


def generate_pdf(pdf_filepath: str, md_filepath: str):
    Converter(pdf_filepath).convert([md_filepath])


def get_highlighted_text(text, highlighted):
    highs = highlighted[0]
    return text[highs[0]: highs[1]]


class MD_Generator:
    """ Generates md file containing examples and translations
    read for md to pdf conversion
    Attributes:
    - filename
    - API object
    """

    def __init__(self, api, filename, words):
        self.API = api
        self.filename = filename
        self.words = words
        self.session = requests.Session()

    def generate(self):
        with MarkdownGenerator(filename=self.filename, enable_write=True) as doc:
            doc.addHeader(level=1, text="Translations")
            for word in self.words:
                # Get Data
                api = self.API(
                    source_text=word,
                    source_lang="de",
                    target_lang="en",
                    req_session=self.session
                )

                # Translations
                translations = []
                for i, data in enumerate(api.get_translations()):
                    if i == 3:
                        break
                    translations.append(data[1])

                # Examples
                examples = []
                for i, (source, target) in enumerate(api.get_examples()):
                    if i == 3:
                        break
                    examples.append(f"{source.text} - {target.text}")

                # wait
                doc.writeTextLine(
                    f'{doc.addBoldedText(api.source_text)} - {", ".join(translations)}')
                doc.addUnorderedList(examples)
