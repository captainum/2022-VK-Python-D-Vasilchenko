# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
# pylint: disable=unused-argument
# pylint: disable=unnecessary-dunder-call
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel

import cProfile
import io
import pstats
from functools import wraps


def profile_deco(func):
    if "profiler" not in func.__dir__():
        setattr(func, "profiler", cProfile.Profile())
        setattr(func, "stream", io.StringIO())

        def print_stat():
            print(func.stream.getvalue())

        setattr(func, "print_stat", print_stat)

    @wraps(func)
    def wrapper(*args, **kwargs):
        func.profiler.enable()
        result = func(*args, **kwargs)
        func.profiler.disable()

        ps = pstats.Stats(func.profiler, stream=func.stream).sort_stats(
            "cumulative"
        )
        ps.print_stats()

        func.profiler.clear()

        return result

    return wrapper


if __name__ == "__main__":

    @profile_deco
    def add(a, b):
        import time

        time.sleep(2)
        return a + b

    add(1, 2)
    add(4, 5)

    add.print_stat()
