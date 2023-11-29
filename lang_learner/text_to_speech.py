'''

from gtts import gTTS
from pydub import AudioSegment


class Voice:
    def __init__(self, source_txt: str, target_txt: str, filename: str):
        self.source_txt = source_txt
        self.target_txt = target_txt
        self.filename = filename

    def generate_mp3(self):
        audio_de = gTTS(text=self.source_txt, lang="de", slow=False)
        audio_en = gTTS(text=self.target_txt, lang="en", slow=False)

        audio_de.save("user/speech_de.mp3")
        audio_en.save("user/speech_en.mp3")

    def merge_audio(self):
        sound_1 = AudioSegment.from_mp3("user/speech_de.mp3")
        sound_2 = AudioSegment.from_mp3("user/speech_en.mp3")

        speech = sound_1 + sound_2
        speech.export(f"{self.filename}.mp3", format="mp3")

    def generate_speech(self):
        self.generate_mp3()
        self.merge_audio()
'''
