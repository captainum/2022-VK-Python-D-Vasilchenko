# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name


import io
import unittest

from filter_file import filter_file
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_cache_capacity_1(self):
        cache = LRUCache(1)

        cache["k1"] = "val1"
        self.assertEqual(cache["k1"], "val1")

        cache["k2"] = "val2"
        self.assertIsNone(cache["k1"])
        self.assertEqual(cache["k2"], "val2")

    def test_cache_capacity_3(self):
        cache = LRUCache(3)

        cache["k1"] = "val1"
        cache["k2"] = "val2"
        cache["k3"] = "val3"

        self.assertEqual(cache["k1"], "val1")
        self.assertEqual(cache["k2"], "val2")
        self.assertEqual(cache["k3"], "val3")
        self.assertIsNone(cache["k4"])

        cache["k4"] = "val4"

        self.assertIsNone(cache["k1"])
        self.assertEqual(cache["k2"], "val2")
        self.assertEqual(cache["k3"], "val3")
        self.assertEqual(cache["k4"], "val4")

        cache["k2"] = "changed_val2"
        cache["k5"] = "val5"

        self.assertEqual(cache["k2"], "changed_val2")
        self.assertIsNone(cache["k3"])
        self.assertEqual(cache["k4"], "val4")
        self.assertEqual(cache["k5"], "val5")

    def test_cache_change_element(self):
        cache = LRUCache(2)

        cache["k1"] = "val1"
        cache["k2"] = "val2"

        cache["k1"] = "changed_val1"
        cache["k3"] = "val3"

        self.assertEqual(cache["k1"], "changed_val1")
        self.assertIsNone(cache["k2"])
        self.assertEqual(cache["k3"], "val3")

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
