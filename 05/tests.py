# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name


import io
import unittest

from filter_file import filter_file
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_cache(self):
        cache = LRUCache(2)

        cache["k1"] = "val1"
        cache["k2"] = "val2"

        self.assertIsNone(cache["k3"])
        self.assertEqual(cache["k2"], "val2")
        self.assertEqual(cache["k1"], "val1")

        cache["k3"] = "val3"
        cache["k1"] = "val11"

        self.assertEqual(cache["k3"], "val3")
        self.assertIsNone(cache["k2"])
        self.assertEqual(cache["k1"], "val11")

    def test_cache_invalid_limit(self):
        self.assertRaises(ValueError, LRUCache, -2)


class TestFilterFile(unittest.TestCase):
    def test_filter_str_path(self):
        found_lines = []
        for line in filter_file("./test.txt", ["роза", "реч", "Валентин"]):
            found_lines.append(line)
        self.assertEqual(
            found_lines, ["а Роза упала на лапу Азора", "Валентин шел и упал"]
        )

    def test_filter(self):
        f = io.StringIO()
        f.writelines(
            [
                "а Роза упала на лапу Азора\n",
                "уронила в речку мячик\n",
                "Валентин шел и упал\n",
            ]
        )
        f.seek(0)
        found_lines = []
        for line in filter_file(f, ["роза", "реч", "Валентин"]):
            found_lines.append(line)
        self.assertEqual(
            found_lines, ["а Роза упала на лапу Азора", "Валентин шел и упал"]
        )
