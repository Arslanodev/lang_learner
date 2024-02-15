import tempfile

from gtts import gTTS
from pydub import AudioSegment


class Voice:
    def __init__(
        self,
        source_txt: str,
        target_txt: str,
        filename: str,
        source_lang: str = "de",
        target_lang: str = "en",
    ):
        self.source_txt = source_txt
        self.source_lang = source_lang
        self.target_txt = target_txt
        self.target_lang = target_lang
        self.filename = filename
        self.tfile_0 = tempfile.NamedTemporaryFile()
        self.tfile_1 = tempfile.NamedTemporaryFile()

    def generate_mp3(self):
        audio_de = gTTS(text=self.source_txt, lang=self.source_lang, slow=False)
        audio_en = gTTS(text=self.target_txt, lang=self.target_lang, slow=False)

        # Slow down
        audio_de.save(self.tfile_0.name)
        audio_en.save(self.tfile_1.name)

    def merge_audio(self):
        sound_1 = AudioSegment.from_mp3(self.tfile_0.name)
        sound_2 = AudioSegment.from_mp3(self.tfile_1.name)
        delay = AudioSegment.silent(duration=1500)

        speech = sound_1 + delay + sound_2
        speech.export(f"{self.filename}.mp3", format="mp3")

    def generate_speech(self):
        self.generate_mp3()
        self.merge_audio()
