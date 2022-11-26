# pylint: disable=use-implicit-booleaness-not-comparison
# pylint: disable=too-many-arguments
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=import-error

import unittest
from typing import Union, List

from parameterized import parameterized

from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def assert_lists_deep_equality(
            self,
            first: Union[CustomList, List],
            second: Union[CustomList, List],
    ):
        self.assertEqual(len(first), len(second))
        for elements in zip(first, second):
            self.assertEqual(elements[0], elements[1])
        self.assertEqual(first, second)

    @parameterized.expand(
        [
            (
                CustomList(),
                [],
                CustomList(),
                CustomList(),
                CustomList(),
            ),
            (
                CustomList([1]),
                [],
                CustomList([1]),
                CustomList([1]),
                CustomList([-1]),
            ),
            (
                CustomList(),
                [1],
                CustomList([1]),
                CustomList([-1]),
                CustomList([1]),
            ),
            (
                CustomList([1, 2, 3]),
                [4, 5, 6],
                CustomList([5, 7, 9]),
                CustomList([-3, -3, -3]),
                CustomList([3, 3, 3]),
            ),
            (
                CustomList([1, 2]),
                [3],
                CustomList([4, 2]),
                CustomList([-2, 2]),
                CustomList([2, -2]),
            ),
            (
                CustomList([1]),
                [2, 3],
                CustomList([3, 3]),
                CustomList([-1, -3]),
                CustomList([1, 3]),
            ),
        ]
    )
    def test_add_sub(
        self, first, second, result_sum, result_sub_l, result_sub_r
    ):
        first_dumped = first[:]
        second_dumped = second[:]

        l_sum = first + second
        self.assert_lists_deep_equality(first, first_dumped)
        self.assert_lists_deep_equality(second, second_dumped)
        self.assert_lists_deep_equality(l_sum, result_sum)

        l_sum = first + CustomList(second)
        self.assert_lists_deep_equality(l_sum, result_sum)

        r_sum = second + first
        self.assert_lists_deep_equality(first, first_dumped)
        self.assert_lists_deep_equality(second, second_dumped)
        self.assert_lists_deep_equality(r_sum, result_sum)

        r_sum = CustomList(second) + first
        self.assert_lists_deep_equality(r_sum, result_sum)

        l_sub = first - second
        self.assert_lists_deep_equality(first, first_dumped)
        self.assert_lists_deep_equality(second, second_dumped)
        self.assert_lists_deep_equality(l_sub, result_sub_l)

        l_sub = first - CustomList(second)
        self.assert_lists_deep_equality(l_sub, result_sub_l)

        r_sub = second - first
        self.assert_lists_deep_equality(first, first_dumped)
        self.assert_lists_deep_equality(second, second_dumped)
        self.assert_lists_deep_equality(r_sub, result_sub_r)

        r_sub = CustomList(second) - first
        self.assert_lists_deep_equality(r_sub, result_sub_r)

        self.assertEqual(len(first), len(first_dumped))
        for elements in zip(first, first_dumped):
            self.assertEqual(elements[0], elements[1])

        self.assertEqual(len(second), len(second_dumped))
        for elements in zip(second, second_dumped):
            self.assertEqual(elements[0], elements[1])

    @parameterized.expand(
        [
            (CustomList(), [], "eq"),
            ([2, 3], CustomList([1]), "neq"),
            (CustomList([1]), [1, 2], "lt"),
            (CustomList([1, 2]), [1, 2], "le"),
            (CustomList([1, 2]), [1, 2, 3], "le"),
            (CustomList([1, 2, 3]), [1, 2, 2], "gt"),
            (CustomList([1, 2, 3]), [1, 2, 3], "ge"),
            (CustomList([1, 2, 3]), [1], "ge"),
        ]
    )
    def test_expressions(self, l_value, r_value, operation_str):
        l_value_dumped = l_value[:]
        r_value_dumped = r_value[:]

        operation = ""
        if operation_str == "eq":
            operation = l_value == r_value
        elif operation_str == "neq":
            operation = l_value != r_value
        elif operation_str == "lt":
            operation = l_value < r_value
        elif operation_str == "le":
            operation = l_value <= r_value
        elif operation_str == "gt":
            operation = l_value > r_value
        else:
            operation = l_value >= r_value

        self.assert_lists_deep_equality(l_value, l_value_dumped)
        self.assert_lists_deep_equality(r_value, r_value_dumped)
        self.assertTrue(operation)

    @parameterized.expand(
        [
            (
                CustomList([]),
                "Elements: []\nSummary: 0",
            ),
            (CustomList([1, 3, 5, -4]), "Elements: [1, 3, 5, -4]\nSummary: 5"),
        ]
    )
    def test_repr(self, lst, representation):
        lst_dumped = lst[:]
        self.assertEqual(str(lst), representation)
        self.assert_lists_deep_equality(lst, lst_dumped)
