import io
import sys
import unittest.mock

from tic_tac import Coordinates, TicTacGame


@unittest.mock.patch("sys.stdout")
class TestTicTacTack(unittest.TestCase):
    def test_make_turn_empty_cell(self, out):
        g = TicTacGame()
        self.assertTrue(g.make_turn("x", Coordinates(1, 1)))

    def test_make_turn_fulled_cell(self, out):
        g = TicTacGame()
        g._board[1][1] = "x"
        self.assertFalse(g.make_turn("o", Coordinates(1, 1)))

    def test_check_winner(self, out):
        g = TicTacGame()
        for stage in [
            [
                ["x", "x", "x"],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                ["x", 0, 0],
                ["x", 0, 0],
                ["x", 0, 0],
            ],
            [
                ["x", 0, 0],
                [0, "x", 0],
                [0, 0, "x"],
            ],
            [
                [0, "x", 0],
                [0, "x", 0],
                [0, "x", 0],
            ],
            [
                [0, 0, "x"],
                [0, "x", 0],
                ["x", 0, 0],
            ],
            [
                [0, 0, "x"],
                [0, 0, "x"],
                [0, 0, "x"],
            ],
            [
                [0, 0, 0],
                ["x", "x", "x"],
                [0, 0, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                ["x", "x", "x"],
            ],
        ]:
            g._board = stage
            self.assertEqual(g.check_winner(), "x")

    def test_check_winner_tie(self, out):
        g = TicTacGame()
        g._board = [
            ["x", "o", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]
        g._turn = 9
        self.assertEqual(g.check_winner(), "-")

    def test_show_board(self, out):
        g = TicTacGame()
        g._board = [
            ["x", "o", 0],
            ["o", "x", 0],
            ["x", 0, "o"],
        ]
        expected = " |0|1|2| \n" "0|x|o| |\n" "1|o|x| |\n" "2|x| |o|\n"

        func_output = io.StringIO()
        sys.stdout = func_output
        g.show_board()
        sys.stdout = sys.__stdout__
        self.assertEqual(func_output.getvalue(), expected)

    def test_validate_input_end_game(self, out):
        g = TicTacGame()
        validated = g.validate_input("-1")
        self.assertEqual(validated, -1)

    def test_validate_correct_input(self, out):
        g = TicTacGame()
        validated = g.validate_input("1, 2")
        self.assertTrue(validated)

    def test_validate_incorrect_input(self, out):
        g = TicTacGame()
        for phrase in [
            "1, 4",
            "s;fkd",
            "sdflk, 3",
            "1, 2, 0",
            "-1, 2" "5",
            "",
        ]:
            validated = g.validate_input(phrase)
            self.assertFalse(validated)

    @unittest.mock.patch(
        "builtins.input", side_effect=["1, 1", "1, 2", "0, 0", "1, 0", "2, 2"]
    )
    def test_game_first_winner(self, out, mock_input):
        g = TicTacGame()
        result = g.game()
        self.assertEqual(result, "Победил первый игрок")

    @unittest.mock.patch(
        "builtins.input",
        side_effect=["1, 1", "1, 1", "0, 1", "2, 2", "0, 0", "2, 0", "0, 2"],
    )
    def test_game_second_winner(self, out, mock_input):
        g = TicTacGame()
        result = g.game()
        self.assertEqual(result, "Победил второй игрок")

    @unittest.mock.patch(
        "builtins.input",
        side_effect=[
            "1, 1",
            "0, 1",
            "2, 2",
            "0, 0",
            "0, 2",
            "1, 2",
            "1, 0",
            "2, 0",
            "2, 1",
        ],
    )
    def test_game_tie(self, out, mock_input):
        g = TicTacGame()
        result = g.game()
        self.assertEqual(result, "Ничья!")

    @unittest.mock.patch(
        "builtins.input", side_effect=["1, 1", "0, 1", "2, 2", "-1"]
    )
    def test_game_exit(self, out, mock_input):
        g = TicTacGame()
        result = g.game()
        self.assertEqual(result, "Игра завершена")
