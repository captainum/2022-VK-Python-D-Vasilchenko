# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-import
# pylint: disable=logging-fstring-interpolation
# pylint: disable=protected-access
# pylint: disable=pointless-statement


import argparse
import logging
import sys
from collections import deque
from typing import Any, Deque, Dict


class LRUCache:
    _logger = logging.getLogger(__file__)
    _logger.setLevel(logging.DEBUG)
    __formatter = logging.Formatter(
        "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s"
    )
    __file_handler = logging.FileHandler("cache.log")
    __file_handler.setLevel(logging.DEBUG)
    __file_handler.setFormatter(__formatter)
    _logger.addHandler(__file_handler)

    def __init__(self, limit: int = 42):
        self._logger.info(f"Creating cache with {limit=}")
        if limit < 1:
            self._logger.error("Limit is less than 1")
            raise ValueError
        self.limit = limit
        self.elements: Deque[Any] = deque()
        self.mapping: Dict[Any, Any] = {}
        self._logger.info("Cache has been created")

    def __getitem__(self, key):
        self._logger.info(f"Get element by {key=}")
        if key in self.mapping:
            self._logger.debug(
                f"Element with {key=} is found, changing priority"
            )
            self.elements.remove(key)
            self.elements.append(key)
            return self.mapping[key]
        self._logger.debug(f"Element with {key=} not found")
        return None

    def __setitem__(self, key, value):
        self._logger.info(f"Add element with {key=}, {value=}")
        if key in self.mapping:
            self._logger.debug(
                f"Element with {key=} is already in cache, changing priority"
            )
            self.elements.remove(key)
            self.elements.append(key)
            self.mapping[key] = value
        else:
            self._logger.debug(f"Element with {key=} is not in cache")
            if len(self.elements) == self.limit:
                self._logger.warning(
                    "Cache is full, pop least recently used element"
                )
                self.mapping.pop(self.elements.popleft())
            self.elements.append(key)
            self.mapping[key] = value
        self._logger.info(f"Successfully added element with {key=}, {value=}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", action="store_true", help="logging to stdout")
    args = parser.parse_args()
    if args.s:
        stdout_handler = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(formatter)

        LRUCache._logger.addHandler(stdout_handler)

    cache = LRUCache(3)

    cache["k1"] = "val1"
    cache["k2"] = "val2"
    cache["k3"] = "val3"

    cache["k2"]
    cache["k4"]

    cache["k4"] = "val4"

    cache["k2"] = "changed_val2"
    cache["k5"] = "val5"
