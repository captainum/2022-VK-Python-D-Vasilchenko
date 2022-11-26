# pylint: disable=unidiomatic-typecheck
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

from typing import List, Union


class CustomList(List):
    def __add__(self, other: Union["CustomList", List]) -> "CustomList":
        min_length = min(len(self), len(other))

        lst = [x + y for x, y in zip(self[:min_length], other[:min_length])]
        lst.extend(self[min_length:])
        lst.extend(other[min_length:])

        return CustomList(lst)

    def __radd__(self, other: List) -> "CustomList":
        return self + other

    def __sub__(self, other: Union["CustomList", List]) -> "CustomList":
        return self + -(CustomList(other) if type(other) is list else other)

    def __rsub__(self, other: List) -> "CustomList":
        return CustomList(other) - self

    def __eq__(self, other: Union["CustomList", List]) -> bool:
        return sum(self) == sum(other)

    def __ne__(self, other: Union["CustomList", List]) -> bool:
        return not self == other

    def __lt__(self, other: Union["CustomList", List]) -> bool:
        return sum(self) < sum(other)

    def __le__(self, other: Union["CustomList", List]) -> bool:
        return sum(self) <= sum(other)

    def __gt__(self, other: Union["CustomList", List]) -> bool:
        return not self <= other

    def __ge__(self, other: Union["CustomList", List]) -> bool:
        return not self < other

    def __neg__(self) -> "CustomList":
        return CustomList([-x for x in self])

    def __str__(self) -> str:
        return (
            f"Elements: {self[:]}\n"
            f"Summary: {sum(self)}"
        )
