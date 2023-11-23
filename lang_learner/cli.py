import click
from pathlib import Path
from lang_learner.pdf_generator import Pdf_generator


@click.command()
@click.argument("words")
def create(words):
    Path("user").mkdir(parents=True, exist_ok=True)
    Pdf_generator(filepath="user/translations.md",
                  words_filepath=words).generate_pdf()


if __name__ == "__main__":
    create()
