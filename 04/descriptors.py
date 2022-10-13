# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

from abc import ABCMeta, abstractmethod


class BaseDescriptor(metaclass=ABCMeta):
    def __init__(self, /, value):
        if self._condition(value):
            self.value = value
        else:
            raise TypeError

    def __set__(self, instance, value):
        if self._condition(value):
            self.value = value
        else:
            raise TypeError

    @abstractmethod
    def _condition(self, value):
        ...

    def __eq__(self, other):
        return self.value == other


class Integer(BaseDescriptor):
    def _condition(self, value):
        return isinstance(value, int)


class CapitalString(BaseDescriptor):
    def _condition(self, value):
        return isinstance(value, str) and value[0].upper() == value[0]


class PositiveInteger(BaseDescriptor):
    def _condition(self, value):
        return isinstance(value, int) and value > 0
