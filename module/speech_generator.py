import os
import uuid
import shutil
import tempfile

from module.text_to_speech import Voice
from reverso_api import ReversoContextAPI


def generate_mp3(source_texts: list, source_lang: str, target_lang: str):
    temp_dir = tempfile.TemporaryDirectory(dir=".")
    zip_dir_name = "voices"

    os.makedirs(os.path.join(temp_dir.name, zip_dir_name))

    obj = ReversoContextAPI(
        source_texts=source_texts,
        source_lang=source_lang,
        target_lang=target_lang,
    ).get_data()
    for translation, _ in obj:
        Voice(
            source_txt=translation.source_word,
            target_txt=translation.translation[0],
            target_lang=target_lang,
            source_lang=source_lang,
            filename=os.path.join(temp_dir.name, zip_dir_name, translation.source_word),
        ).generate_speech()

    unique_filename = str(uuid.uuid4())
    shutil.make_archive(
        base_name=f"file_storage/{unique_filename}",
        format="zip",
        root_dir=temp_dir.name,
        base_dir="voices",
    )
    temp_dir.cleanup()

    return unique_filename


