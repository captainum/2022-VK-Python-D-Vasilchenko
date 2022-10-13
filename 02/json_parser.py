import json
from typing import Any, Callable, Dict, List, Optional


class NoKeywordCallbackError(ValueError):
    ...


def parse_json(
    json_str: str,
    required_fields: List[str],
    keywords: List[str],
    keyword_callback: Optional[Callable[[str], Any]],
):
    if not keyword_callback:
        raise NoKeywordCallbackError

    parsed_json: Dict[str, str] = json.loads(json_str)
    intersection = set(parsed_json.keys()).intersection(required_fields)
    for key in intersection:
        if parsed_json[key] in keywords:
            keyword_callback(key)
