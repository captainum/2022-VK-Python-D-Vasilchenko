# pylint: disable=consider-using-f-string
# pylint: disable=invalid-name

from typing import List, Literal, NamedTuple, Optional, Union


class Coordinates(NamedTuple):
    x: int
    y: int


class TicTacGame:
    def __init__(self):
        self._board: List[List[Union[int, Literal["x", "o"]]]] = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self._turn = 0
        self._winning_positions = [
            ((0, 0), (0, 1), (0, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 0), (1, 1), (2, 2)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 1), (2, 0)),
            ((0, 2), (1, 2), (2, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
        ]

    def make_turn(self, player: Literal["x", "o"], coordinates: Coordinates):
        if self._board[coordinates.y][coordinates.x] == 0:
            self._board[coordinates.y][coordinates.x] = player
            self._turn += 1
            return True
        return False

    def check_winner(self) -> Optional[Literal["x", "o", "-"]]:
        for position in self._winning_positions:
            values = set()
            for y, x in position:
                values.add(self._board[y][x])
            if ("x" in values or "o" in values) and len(values) == 1:
                return "x" if "x" in values else "o"  # type: ignore
        if self._turn == 9:
            return "-"
        return None

    def show_board(self):
        print(" |0|1|2| ")
        for y in range(3):
            print(f"{y}|", end="")
            for x in range(3):
                print(
                    f"{self._board[y][x] if self._board[y][x] != 0 else ' '}|",
                    end="",
                )
            print()

    def validate_input(self, string):
        parsed = string.split(", ")
        try:
            if len(parsed) < 1 or len(parsed) > 2:
                raise ValueError
            if len(parsed) == 1:
                if int(parsed[0]) == -1:
                    return -1
                raise ValueError
            x, y = parsed
            x, y = int(x), int(y)
            if not (0 <= x <= 2 and 0 <= y <= 2):
                raise ValueError
            return True
        except ValueError:
            print("Ошибка ввода! Попробуйте еще раз :(")
            return False

    def game(self):
        print(
            "Координаты хода задаются в формате 'x, y' (без кавычек)\n"
            "Для выхода введите -1"
        )
        player: Literal["x", "o"] = "x"
        while True:
            self.show_board()
            string = input("Введите координаты: ")
            validated = self.validate_input(string)
            if validated == -1:
                break
            if validated:
                x, y = [int(k) for k in string.split(", ")]

                if not self.make_turn(player, Coordinates(x, y)):
                    print("Эта ячейка уже занята :(")
                    continue

                winner = self.check_winner()
                if winner:
                    self.show_board()
                    if winner == "-":
                        return "Ничья!"
                    return "Победил {} игрок".format(
                        "первый" if winner == "x" else "второй"
                    )
                player = "x" if player == "o" else "o"  # type: ignore

        return "Игра завершена"
