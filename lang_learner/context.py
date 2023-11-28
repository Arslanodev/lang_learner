"""Reverso Context (context.reverso.net) API for Python"""
import json
import asyncio

from typing import List, Tuple, Iterator
from collections import namedtuple

import aiohttp

from bs4 import BeautifulSoup

__all__ = ["ReversoContextAPI"]

HEADERS = {"User-Agent": "Mozilla/5.0",
           "Content-Type": "application/json; charset=UTF-8"
           }

WordUsageExample = namedtuple(
    "WordUsageExample", ("source_text", "target_text"))

Translation = namedtuple("Translation", ("source_word", "translation"))


class ReversoContextAPI(object):
    """Class for Reverso Context API (https://voice.reverso.net/)

    Attributes:
        source_text
        target_text
        source_lang
        target_lang
        page_count

    Methods:
        get_translations()
        get_examples()

    """

    def __init__(self,
                 source_texts: list = ["пример"],
                 target_text: str = "",
                 source_lang: str = "de",
                 target_lang: str = "en",
                 examples_count: int = 3,
                 trans_count: int = 3):

        self.examples_count = examples_count
        self.trans_count = trans_count

        self.source_texts = source_texts
        self.target_text = target_text
        self.source_lang = source_lang
        self.target_lang = target_lang

    def get_translations(self, response: dict, word: str) -> Translation:
        "Returns Translation namedTuple"
        trans_ls = []
        for index, item in enumerate(response["dictionary_entry_list"]):
            trans_ls.append(item['term'])

            if index == self.trans_count - 1:
                break

        return Translation(source_word=word, translation=trans_ls)

    def get_examples(self, response: dict) -> List[WordUsageExample]:
        """Returns list of WordUsageExample"""
        examples = []
        for index, ex in enumerate(response['list']):
            source = BeautifulSoup(ex["s_text"], features="lxml")
            target = BeautifulSoup(ex["t_text"], features="lxml")
            example = WordUsageExample(
                source_text=source.text,
                target_text=target.text
            )
            examples.append(example)
            if index == self.examples_count-1:
                break

        return examples

    async def do_post(self,
                      session: aiohttp.ClientSession,
                      url: str,
                      word: List[str]
                      ) -> Tuple[Translation, List[WordUsageExample]]:

        post_data = json.dumps({
            "source_text": word,
            "target_text": "",
            "source_lang": self.source_lang,
            "target_lang": self.target_lang,
        })
        async with session.post(url=url, data=post_data) as response:
            response = await response.json()

            translations = self.get_translations(response, word)
            examples = self.get_examples(response)

            return translations, examples

    async def make_words(self) -> Iterator[str]:
        for word in self.source_texts:
            yield word

    async def async_post_request(self) -> List[tuple]:
        """Performing asynchronous post request to given url"""

        url = "https://context.reverso.net/bst-query-service"
        async with aiohttp.ClientSession(
                headers=HEADERS,
                connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            post_tasks = []
            async for w in self.make_words():
                post_tasks.append(self.do_post(session, url, w))

            res = await asyncio.gather(*post_tasks)

            return res

    def get_data(self) -> List[tuple]:
        """Runs async post request and return response"""
        response = asyncio.run(self.async_post_request())

        return response
