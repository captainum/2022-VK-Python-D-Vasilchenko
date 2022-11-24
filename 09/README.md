## Домашнее задание №9

### 1. Сравнение использования weakref и слотов

````
Graph (create): 5.536394834518433
Graph (get_attr): 2.3670339584350586
Graph (set_attr): 3.1242151260375977
Graph (del_attr): 0.8264782428741455

GraphSlots (create): 4.280614137649536
GraphSlots (get_attr): 2.2273969650268555
GraphSlots (set_attr): 2.7805721759796143
GraphSlots (del_attr): 0.15107297897338867

GraphWeakrefs (create): 6.767807960510254
GraphWeakrefs (get_attr): 2.9285640716552734
GraphWeakrefs (set_attr): 3.6011829376220703
GraphWeakrefs (del_attr): 0.7031450271606445
````

Видно, что по быстродействию лучше всего проходит способ с использованием slots,
хуже всего - с использованием слабых ссылок.

### 2. Профилирование

#### Память
````
Graph
Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13     13.2 MiB     13.2 MiB           1   def create_graphs(GraphType, param_1, param_2, param_3):
    14     27.5 MiB     14.3 MiB       85003       return [GraphType(param_1, param_2, param_3) for _ in range(N)]


Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    17     27.5 MiB     27.5 MiB           1   def get_attr(graphs):
    18     27.5 MiB      0.0 MiB       85001       for graph in graphs:
    19     27.5 MiB      0.0 MiB       85000           if "GraphWeakrefs" in graph.__str__():
    20                                                     graph.dots(), graph.lines(), graph.signatures()
    21                                                 else:
    22     27.5 MiB      0.0 MiB       85000               graph.dots, graph.lines, graph.signatures


Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    25     27.5 MiB     27.5 MiB           1   def set_attr(graphs):
    26     27.5 MiB      0.0 MiB       85001       for graph in graphs:
    27     27.5 MiB      0.0 MiB       85000           if "GraphWeakrefs" in graph.__str__():
    28                                                     graph.dots().add((5, 5))
    29                                                     graph.lines().add((1, 2, 3, 4))
    30                                                     graph.signatures().add("new_signature")
    31                                                 else:
    32     27.5 MiB      0.0 MiB       85000               graph.dots.add((5, 5))
    33     27.5 MiB      0.0 MiB       85000               graph.lines.add((1, 2, 3, 4))
    34     27.5 MiB      0.0 MiB       85000               graph.signatures.add("new_signature")


Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37     27.5 MiB     27.5 MiB           1   def del_attr(graphs):
    38     41.9 MiB      0.0 MiB       85001       for graph in graphs:
    39     41.9 MiB     14.4 MiB       85000           del graph.dots



GraphSlots
Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13     41.9 MiB     41.9 MiB           1   def create_graphs(GraphType, param_1, param_2, param_3):
    14     47.9 MiB      5.9 MiB       85003       return [GraphType(param_1, param_2, param_3) for _ in range(N)]


Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    17     20.9 MiB     20.9 MiB           1   def get_attr(graphs):
    18     20.9 MiB      0.0 MiB       85001       for graph in graphs:
    19     20.9 MiB      0.0 MiB       85000           if "GraphWeakrefs" in graph.__str__():
    20                                                     graph.dots(), graph.lines(), graph.signatures()
    21                                                 else:
    22     20.9 MiB      0.0 MiB       85000               graph.dots, graph.lines, graph.signatures


Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    25     20.9 MiB     20.9 MiB           1   def set_attr(graphs):
    26     20.9 MiB      0.0 MiB       85001       for graph in graphs:
    27     20.9 MiB      0.0 MiB       85000           if "GraphWeakrefs" in graph.__str__():
    28                                                     graph.dots().add((5, 5))
    29                                                     graph.lines().add((1, 2, 3, 4))
    30                                                     graph.signatures().add("new_signature")
    31                                                 else:
    32     20.9 MiB      0.0 MiB       85000               graph.dots.add((5, 5))
    33     20.9 MiB      0.0 MiB       85000               graph.lines.add((1, 2, 3, 4))
    34     20.9 MiB      0.0 MiB       85000               graph.signatures.add("new_signature")


Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37     20.9 MiB     20.9 MiB           1   def del_attr(graphs):
    38     20.9 MiB      0.0 MiB       85001       for graph in graphs:
    39     20.9 MiB      0.0 MiB       85000           del graph.dots



GraphWeakrefs
Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13     20.9 MiB     20.9 MiB           1   def create_graphs(GraphType, param_1, param_2, param_3):
    14     34.0 MiB     13.2 MiB       85003       return [GraphType(param_1, param_2, param_3) for _ in range(N)]


Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    17     29.0 MiB     29.0 MiB           1   def get_attr(graphs):
    18     29.0 MiB      0.0 MiB       85001       for graph in graphs:
    19     29.0 MiB      0.0 MiB       85000           if "GraphWeakrefs" in graph.__str__():
    20     29.0 MiB      0.0 MiB       85000               graph.dots(), graph.lines(), graph.signatures()
    21                                                 else:
    22                                                     graph.dots, graph.lines, graph.signatures


Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    25     29.0 MiB     29.0 MiB           1   def set_attr(graphs):
    26     29.0 MiB      0.0 MiB       85001       for graph in graphs:
    27     29.0 MiB      0.0 MiB       85000           if "GraphWeakrefs" in graph.__str__():
    28     29.0 MiB      0.0 MiB       85000               graph.dots().add((5, 5))
    29     29.0 MiB      0.0 MiB       85000               graph.lines().add((1, 2, 3, 4))
    30     29.0 MiB      0.0 MiB       85000               graph.signatures().add("new_signature")
    31                                                 else:
    32                                                     graph.dots.add((5, 5))
    33                                                     graph.lines.add((1, 2, 3, 4))
    34                                                     graph.signatures.add("new_signature")


Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37     29.0 MiB     29.0 MiB           1   def del_attr(graphs):
    38     43.2 MiB      0.0 MiB       85001       for graph in graphs:
    39     43.2 MiB     14.2 MiB       85000           del graph.dots
````

Видно, что по памяти лучше всего также подходит способ с использованием slots.

#### Время

````
Graph
         5000003 function calls in 6.002 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    6.002    6.002 main.py:13(create_graphs)
        1    2.933    2.933    6.002    6.002 main.py:14(<listcomp>)
  5000000    3.069    0.000    3.069    0.000 /Users/dmitry.vasilchenko/education/2022-VK-Python-D-Vasilchenko/09/classes.py:18(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         2 function calls in 2.581 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.581    2.581    2.581    2.581 main.py:17(get_attr)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         15000002 function calls in 5.146 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    3.993    3.993    5.146    5.146 main.py:25(set_attr)
 15000000    1.153    0.000    1.153    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         2 function calls in 0.708 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.708    0.708    0.708    0.708 main.py:37(del_attr)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



GraphSlots
         5000003 function calls in 4.524 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    4.524    4.524 main.py:13(create_graphs)
        1    3.715    3.715    4.524    4.524 main.py:14(<listcomp>)
  5000000    0.809    0.000    0.809    0.000 /Users/dmitry.vasilchenko/education/2022-VK-Python-D-Vasilchenko/09/classes.py:27(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         2 function calls in 2.432 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.432    2.432    2.432    2.432 main.py:17(get_attr)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         15000002 function calls in 5.068 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    3.896    3.896    5.068    5.068 main.py:25(set_attr)
 15000000    1.171    0.000    1.171    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         2 function calls in 0.155 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.155    0.155    0.155    0.155 main.py:37(del_attr)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



GraphWeakrefs
         5000003 function calls in 7.469 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    7.469    7.469 main.py:13(create_graphs)
        1    1.898    1.898    7.469    7.469 main.py:14(<listcomp>)
  5000000    5.571    0.000    5.571    0.000 /Users/dmitry.vasilchenko/education/2022-VK-Python-D-Vasilchenko/09/classes.py:34(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         2 function calls in 3.195 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    3.195    3.195    3.195    3.195 main.py:17(get_attr)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         15000002 function calls in 5.780 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    4.610    4.610    5.780    5.780 main.py:25(set_attr)
 15000000    1.169    0.000    1.169    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         2 function calls in 0.710 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.710    0.710    0.710    0.710 main.py:37(del_attr)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
````

Результаты аналогичны первому пункту.