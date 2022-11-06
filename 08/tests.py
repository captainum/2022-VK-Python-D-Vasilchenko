# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
# pylint: disable=unused-argument


import unittest.mock

import aiohttp
import aiounittest
import asynctest

from fetcher import Fetcher


class TestFetcher(aiounittest.AsyncTestCase):
    def setUp(self) -> None:
        self.fetcher = Fetcher(2)

    @asynctest.mock.patch("aiohttp.ClientSession")
    async def test_fetch_url(self, client):
        await self.fetcher._fill_q(("https://www.python.org/",))
        self.assertEqual(self.fetcher.q.qsize(), 1)

        async with aiohttp.ClientSession() as session:
            with self.assertRaises(AssertionError):
                await self.fetcher._fetch_url(session)
        self.assertEqual(self.fetcher.q.qsize(), 0)

    @unittest.mock.patch("fetcher.Fetcher._fill_q")
    @unittest.mock.patch("fetcher.Fetcher._fetch_url")
    async def test_fetch_urls(self, fetch_url, fill_q):
        urls = (
            "https://ru.wikipedia.org/wiki/Kimberly",
            "https://ru.wikipedia.org/wiki/Brenda",
            "https://ru.wikipedia.org/wiki/Amanda",
            "https://ru.wikipedia.org/wiki/Douglas",
            "https://ru.wikipedia.org/wiki/Jacob",
        )
        await self.fetcher.fetch_urls(*urls)

        fetch_url.assert_awaited()
        fill_q.assert_awaited()
        self.assertEqual(len(fetch_url.call_args_list), 2)
        self.assertEqual(len(fill_q.call_args_list), 2)
        self.assertEqual(fill_q.call_args_list[0].args[0], urls[:2])
        self.assertEqual(fill_q.call_args_list[1].args[0], urls[2:])
        self.assertEqual(self.fetcher.q.qsize(), 0)
