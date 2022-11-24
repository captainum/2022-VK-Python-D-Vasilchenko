# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
# pylint: disable=unused-argument
# pylint: disable=invalid-name
# pylint: disable=unnecessary-dunder-call
# pylint: disable=expression-not-assigned
# pylint: disable=pointless-statement

import cProfile
import io
import pstats
from time import time

from memory_profiler import profile

from classes import Graph, GraphSlots, GraphWeakrefs

N = 5_000_000


def create_graphs(GraphType, param_1, param_2, param_3):
    return [GraphType(param_1, param_2, param_3) for _ in range(N)]


def get_attr(graphs):
    for graph in graphs:
        if "GraphWeakrefs" in graph.__str__():
            graph.dots(), graph.lines(), graph.signatures()
        else:
            graph.dots, graph.lines, graph.signatures


def set_attr(graphs):
    for graph in graphs:
        if "GraphWeakrefs" in graph.__str__():
            graph.dots().add((5, 5))
            graph.lines().add((1, 2, 3, 4))
            graph.signatures().add("new_signature")
        else:
            graph.dots.add((5, 5))
            graph.lines.add((1, 2, 3, 4))
            graph.signatures.add("new_signature")


def del_attr(graphs):
    for graph in graphs:
        del graph.dots


def timings():
    param_1, param_2, param_3 = (
        {(1, 1), (2, 2)},
        {(0, 0, 1, 1)},
        {"title_1", "title_2"},
    )

    for type_class in [Graph, GraphSlots, GraphWeakrefs]:
        start_time = time()
        lst = create_graphs(type_class, param_1, param_2, param_3)
        end_time = time()
        print(f"{type_class.__name__} (create):", end_time - start_time)

        for func in [get_attr, set_attr, del_attr]:
            start_time = time()
            func(lst)
            end_time = time()
            print(
                f"{type_class.__name__} ({func.__name__}):",
                end_time - start_time,
            )

        print()


def profile_memory():
    s_graphs, s_graphs_slots, s_graphs_weakrefs = (
        io.StringIO(),
        io.StringIO(),
        io.StringIO(),
    )
    param_1, param_2, param_3 = (
        {(1, 1), (2, 2)},
        {(0, 0, 1, 1)},
        {"title_1", "title_2"},
    )

    for type_class, s in [
        (Graph, s_graphs),
        (GraphSlots, s_graphs_slots),
        (GraphWeakrefs, s_graphs_weakrefs),
    ]:
        lst = profile(create_graphs, s)(type_class, param_1, param_2, param_3)
        for func in [get_attr, set_attr, del_attr]:
            profile(func, s)(lst)

    for type_class, s in [
        ("Graph", s_graphs),
        ("GraphSlots", s_graphs_slots),
        ("GraphWeakrefs", s_graphs_weakrefs),
    ]:
        print(type_class, s.getvalue(), sep="\n")


def profile_time():
    s_graphs, s_graphs_slots, s_graphs_weakrefs = (
        io.StringIO(),
        io.StringIO(),
        io.StringIO(),
    )
    param_1, param_2, param_3 = (
        {(1, 1), (2, 2)},
        {(0, 0, 1, 1)},
        {"title_1", "title_2"},
    )

    for type_class, s in [
        (Graph, s_graphs),
        (GraphSlots, s_graphs_slots),
        (GraphWeakrefs, s_graphs_weakrefs),
    ]:
        pr = cProfile.Profile()
        pr.enable()
        lst = create_graphs(type_class, param_1, param_2, param_3)
        pr.disable()
        sortby = "cumulative"
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()

        for func in [get_attr, set_attr, del_attr]:
            pr = cProfile.Profile()
            pr.enable()
            func(lst)
            pr.disable()
            sortby = "cumulative"
            ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
            ps.print_stats()

    for type_class, s in [
        ("Graph", s_graphs),
        ("GraphSlots", s_graphs_slots),
        ("GraphWeakrefs", s_graphs_weakrefs),
    ]:
        print(type_class, s.getvalue(), sep="\n")


if __name__ == "__main__":
    timings()
    profile_memory()
    profile_time()
