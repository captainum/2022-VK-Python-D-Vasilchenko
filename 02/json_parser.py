import json
from typing import Any, Callable, Dict, List


def parse_json(
    json_str: str,
    required_fields: List[str],
    keywords: List[str],
    keyword_callback: Callable[[str], Any],
):
    parsed_json: Dict[str, str] = json.loads(json_str)
    intersection = set(parsed_json.keys()).intersection(required_fields)
    for key in intersection:
        if parsed_json[key] in keywords:
            keyword_callback(key)
