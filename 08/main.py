# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=unspecified-encoding
# pylint: disable=invalid-name


import argparse
import asyncio
import sys

from fetcher import Fetcher


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "c",
        type=int,
    )
    parser.add_argument(
        "file",
        type=str,
    )

    args = parser.parse_args(sys.argv[1:])

    fetcher = Fetcher(args.c)
    with open(args.file, "r") as f:
        urls = tuple(map(str.strip, f.readlines()))

    await fetcher.fetch_urls(*urls)


if __name__ == "__main__":
    asyncio.run(main())
