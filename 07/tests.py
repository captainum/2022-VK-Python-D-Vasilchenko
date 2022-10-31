# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=redundant-keyword-arg
# pylint: disable=wrong-import-order


import unittest
from typing import Tuple, List

from matrix_py import matrix_py
from parameterized import parameterized
import time
import ctypes
import numpy as np


class TestMatrix(unittest.TestCase):
    def setUp(self) -> None:
        libc = ctypes.CDLL('./matrix_c.so')
        self.matrix_calc = libc.matrix_calc

        nd_pointer_2 = np.ctypeslib.ndpointer(
            dtype=ctypes.c_int,
            ndim=2,
            flags="C"
        )

        self.matrix_calc.argtypes = [
            nd_pointer_2,
            nd_pointer_2,
            nd_pointer_2,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int
        ]
        self.matrix_calc.restype = nd_pointer_2

    @parameterized.expand(
        [
            (
                [],
                [],
                (0, 0, 0),
                []
            ),
            (
                [
                    1
                ],
                [
                    1
                ],
                (1, 1, 1),
                [
                    1
                ]
            ),
            (
                [
                    1, 0
                ],
                [
                    1,
                    0,
                ],
                (1, 2, 1),
                [1]
            ),
            (
                [
                    1,
                    0,
                ],
                [
                    1, 0
                ],
                (2, 1, 2),
                [
                    1, 0,
                    0, 0,
                ]
            ),
            (
                [
                    1, 2, 3,
                    4, 5, 6,
                    7, 8, 9,
                ],
                [
                    9, 8, 7,
                    6, 5, 4,
                    3, 2, 1,
                ],
                (3, 3, 3),
                [
                    30, 24, 18,
                    84, 69, 54,
                    138, 114, 90,
                ],
            ),
        ]
    )
    def test_matrix_calculation(
            self,
            matrix_1: List[int],
            matrix_2: List[int],
            shapes: Tuple[int, int, int],
            expected: List[int]
    ):
        n, k, m = shapes

        matrix_3 = [0] * n * m

        np_matrix_1 = np.array(
            matrix_1,
            dtype=ctypes.c_int
        ).reshape((n, k), order="C")
        np_matrix_2 = np.array(
            matrix_2, dtype=ctypes.c_int
        ).reshape((k, m), order="C")

        matrix_py(matrix_1, matrix_2, matrix_3, n, k, m)
        assert matrix_3 == expected

        matrix_3 = [0] * n * m
        np_matrix_3 = np.array(
            matrix_3, dtype=ctypes.c_int
        ).reshape((n, m), order="C")

        self.matrix_calc(np_matrix_1, np_matrix_2, np_matrix_3, n, k, m)
        assert np_matrix_3.reshape(1, n * m, order="C").tolist()[0] == expected

    @parameterized.expand(
        [
            (
                    [1] * 10000,
                    [1] * 10000,
                    (100, 100, 100),
            ),
        ]
    )
    def test_matrix_timings(
            self,
            matrix_1: List[int],
            matrix_2: List[int],
            shapes: Tuple[int, int, int]
    ):
        n, k, m = shapes

        matrix_3 = [0] * n * m

        np_matrix_1 = np.array(
            matrix_1, dtype=ctypes.c_int
        ).reshape((n, k), order="C")
        np_matrix_2 = np.array(
            matrix_2, dtype=ctypes.c_int
        ).reshape((k, m), order="C")

        start_py = time.time()
        matrix_py(matrix_1, matrix_2, matrix_3, n, k, m)
        stop_py = time.time()

        matrix_3 = [0] * n * m
        np_matrix_3 = np.array(
            matrix_3, dtype=ctypes.c_int
        ).reshape((n, m), order="C")

        start_C = time.time()
        self.matrix_calc(np_matrix_1, np_matrix_2, np_matrix_3, n, k, m)
        stop_C = time.time()

        assert stop_C - start_C < stop_py - start_py
