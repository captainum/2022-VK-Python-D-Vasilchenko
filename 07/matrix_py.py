# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=too-many-arguments


from typing import List


def matrix_py(
    a: List[int], b: List[int], c: List[int], n: int, k: int, m: int
):
    for i in range(n):
        for j in range(m):
            for ll in range(k):
                c[i * m + j] += a[i * k + ll] * b[ll * m + j]
