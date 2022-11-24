# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
# pylint: disable=unused-argument
# pylint: disable=too-few-public-methods

import weakref


class Dots(set):
    ...


class Lines(set):
    ...


class Signatures(set):
    ...


class Graph:
    def __init__(self, dots, lines, signatures):
        self.dots = dots
        self.lines = lines
        self.signatures = signatures


class GraphSlots:
    __slots__ = ("dots", "lines", "signatures")

    def __init__(self, dots, lines, signatures):
        self.dots = dots
        self.lines = lines
        self.signatures = signatures


class GraphWeakrefs:
    def __init__(self, dots, lines, signatures):
        self.dots = weakref.ref(dots)
        self.lines = weakref.ref(lines)
        self.signatures = weakref.ref(signatures)
