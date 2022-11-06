# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods


import asyncio
from typing import Tuple

import aiohttp


class Fetcher:
    def __init__(self, c: int):
        self.c = c
        self.q: asyncio.Queue = asyncio.Queue()

    async def _fill_q(self, urls: Tuple[str, ...]):
        for url in urls:
            await self.q.put(url)

    async def _fetch_url(self, session):
        while not self.q.empty():
            url = await self.q.get()
            try:
                async with session.get(url) as resp:
                    assert resp.status in (200, 404)
            finally:
                self.q.task_done()

    async def fetch_urls(self, *urls: str):
        q_tasks = [
            asyncio.create_task(
                self._fill_q(
                    urls[
                        i * len(urls) // self.c: (i + 1) * len(urls) // self.c
                    ]
                )
            )
            for i in range(self.c)
        ]
        await asyncio.gather(*q_tasks)

        async with aiohttp.ClientSession() as session:
            workers = [
                asyncio.create_task(self._fetch_url(session))
                for _ in range(self.c)
            ]
            await asyncio.gather(*workers)
