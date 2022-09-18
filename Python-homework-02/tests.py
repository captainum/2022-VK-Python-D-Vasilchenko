import json
import unittest
from unittest.mock import Mock

from faker import Faker

from json_parser import parse_json


fake = Faker()


class TestJsonParser(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_func = Mock()

        self.first_names = [fake.first_name() for _ in range(10)]
        self.last_names = [fake.last_name() for _ in range(10)]
        self.json_to_parse = json.dumps(
            dict(zip(self.last_names, self.first_names))
        )

    def test_bad_json_str(self):
        for string in (
            "",
            "{",
            "]",
            "foo bar",
        ):
            self.assertRaises(
                json.decoder.JSONDecodeError,
                parse_json,
                json_str=string,
                required_fields=self.last_names,
                keywords=self.first_names,
                keyword_callback=self.mock_func,
            )
            self.assertEqual(self.mock_func.call_count, 0)

    def test_empty_required_fields(self):
        parse_json(
            json_str=self.json_to_parse,
            required_fields=[],
            keywords=self.first_names[::2],
            keyword_callback=self.mock_func,
        )

        self.assertEqual(self.mock_func.call_count, 0)

    def test_empty_keywords(self):
        parse_json(
            json_str=self.json_to_parse,
            required_fields=self.last_names[::2],
            keywords=[],
            keyword_callback=self.mock_func,
        )

        self.assertEqual(self.mock_func.call_count, 0)

    def test_callback(self):
        parse_json(
            json_str=self.json_to_parse,
            required_fields=self.last_names[::2],
            keywords=self.first_names[::2],
            keyword_callback=self.mock_func,
        )

        self.assertEqual(self.mock_func.call_count, 5)

    def test_callback_not_called(self):
        parse_json(
            json_str=self.json_to_parse,
            required_fields=self.last_names[::2],
            keywords=self.first_names[1::2],
            keyword_callback=self.mock_func,
        )

        self.assertEqual(self.mock_func.call_count, 0)
