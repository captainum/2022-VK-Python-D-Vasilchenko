# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
# pylint: disable=unused-argument
# pylint: disable=unnecessary-dunder-call
# pylint: disable=invalid-name

import cProfile
import io
import pstats
from functools import wraps
from time import time


def profile_deco(func):
    if "stats" not in func.__dir__():
        setattr(func, "stats", {})

        def print_stats():
            for start_time, stats in func.stats.items():
                print(
                    f"START_TIME: {start_time}", stats.getvalue(), sep="\n\n"
                )

        setattr(func, "print_stats", print_stats)

    @wraps(func)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()

        start_time = time()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()

        s = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()

        func.stats[start_time] = s

        return result

    return wrapper
