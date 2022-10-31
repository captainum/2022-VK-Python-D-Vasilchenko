## Домашнее задание №7

### Компиляция .so файла

`gcc -fPIC -shared -o matrix_c.so matrix_c.c`

### Запуск тестов

`coverage run -m unittest tests.py`

### Просмотр отчета покрытия

`coverage report --show-missing`

### Отчет покрытия
````
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
matrix_py.py       6      0   100%
tests.py          41      0   100%
--------------------------------------------
TOTAL             47      0   100%
````