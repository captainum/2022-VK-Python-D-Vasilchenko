# pylint: disable=use-implicit-booleaness-not-comparison
# pylint: disable=too-many-arguments
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=import-error

import unittest

from parameterized import parameterized

from custom_list import CustomList


class TestCustomList(unittest.TestCase):
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
        self.assertEqual(first + second, result_sum)
        self.assertEqual(first + CustomList(second), result_sum)

        self.assertEqual(second + first, result_sum)
        self.assertEqual(CustomList(second) + first, result_sum)

        self.assertEqual(first - second, result_sub_l)
        self.assertEqual(first - CustomList(second), result_sub_l)

        self.assertEqual(second - first, result_sub_r)
        self.assertEqual(CustomList(second) - first, result_sub_r)

    def test_expressions(self):
        self.assertTrue(CustomList() == [])
        self.assertTrue([2, 3] != CustomList([1]))

        self.assertTrue(CustomList([1]) < [1, 2])

        self.assertTrue(CustomList([1, 2]) <= [1, 2])
        self.assertTrue(CustomList([1, 2]) <= [1, 2, 3])

        self.assertTrue(CustomList([1, 2, 3]) > [1, 2, 2])

        self.assertTrue(CustomList([1, 2, 3]) >= [1, 2, 3])
        self.assertTrue(CustomList([1, 2, 3]) >= [1])

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
        self.assertEqual(str(lst), representation)
