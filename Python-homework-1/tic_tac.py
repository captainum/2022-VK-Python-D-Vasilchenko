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

    def make_turn(self, player: Literal["x", "o"], coordinates: Coordinates):
        if self._board[coordinates.y][coordinates.x] == 0:
            self._board[coordinates.y][coordinates.x] = player
            self._turn += 1
            return True
        else:
            return False

    def check_winner(self) -> Optional[Literal["x", "o", "-"]]:
        if (
            self._board[0][0] == self._board[0][1] == self._board[0][2] != 0
            or self._board[0][0] == self._board[1][0] == self._board[2][0] != 0
            or self._board[0][0] == self._board[1][1] == self._board[2][2] != 0
        ):
            return self._board[0][0]
        elif self._board[0][1] == self._board[1][1] == self._board[2][1] != 0:
            return self._board[0][1]
        elif (
            self._board[0][2] == self._board[1][1] == self._board[2][0] != 0
            or self._board[0][2] == self._board[1][2] == self._board[2][2] != 0
        ):
            return self._board[0][2]
        elif self._board[1][0] == self._board[1][1] == self._board[1][2] != 0:
            return self._board[1][0]
        elif self._board[2][0] == self._board[2][1] == self._board[2][2] != 0:
            return self._board[2][0]
        elif self._turn == 9:
            return "-"

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
                else:
                    raise ValueError
            else:
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
            elif validated:
                x, y = [int(k) for k in string.split(", ")]

                if not self.make_turn(player, Coordinates(x, y)):
                    print("Эта ячейка уже занята :(")
                    continue

                winner = self.check_winner()
                if winner:
                    self.show_board()
                    if winner == "-":
                        return "Ничья!"
                    else:
                        return "Победил {} игрок".format(
                            "первый" if winner == "x" else "второй"
                        )
                player = "x" if player == "o" else "o"  # type: ignore

        return "Игра завершена"
