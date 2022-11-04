## Домашнее задание №6

## Запуск сервера

`python -m server -w num -k num`

## Запуск клиента

`python -m client -M num --file client/urls.txt`

### Запуск тестов

`coverage run -m unittest tests.py`

### Просмотр отчета покрытия

`coverage report --show-missing`

### Отчет покрытия
````
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
client/__init__.py       0      0   100%
client/client.py        23      0   100%
server/__init__.py       0      0   100%
server/server.py        43      0   100%
tests.py                45      0   100%
--------------------------------------------------
TOTAL                  111      0   100%
````