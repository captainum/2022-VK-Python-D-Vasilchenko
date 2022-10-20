# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-import


from collections import deque
from typing import Any, Deque, Dict


class LRUCache:
    def __init__(self, limit: int = 42):
        if limit < 1:
            raise ValueError
        self.limit = limit
        self.elements: Deque[Any] = deque()
        self.mapping: Dict[Any, Any] = {}

    def __getitem__(self, key):
        if key in self.mapping:
            self.elements.remove(key)
            self.elements.append(key)
            return self.mapping[key]
        return None

    def __setitem__(self, key, value):
        if key in self.mapping:
            self.elements.remove(key)
            self.elements.append(key)
            self.mapping[key] = value
        else:
            if len(self.elements) == self.limit:
                self.mapping.pop(self.elements.popleft())
            self.elements.append(key)
            self.mapping[key] = value
