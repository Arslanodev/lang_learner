from pydantic import BaseModel


class Data(BaseModel):
    source_texts: list[str]
    source_lang: str
    target_lang: str
