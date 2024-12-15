import math

from board import Board


def calc_score(board: Board) -> float:
    """評価点を算出

    Args:
        board (Board): 盤情報

    Returns:
        float: 算出結果
    """
    result = 0.0
    histgram = board.hist()
    for key in histgram:
        categorized_list = histgram[key]
        for categorized_i1 in range(len(categorized_list)):
            for categorized_i2 in range(categorized_i1, len(categorized_list)):
                categorized_list[categorized_i1]
                result += math.sqrt(
                    math.pow(
                        categorized_list[categorized_i1][0] -
                        categorized_list[categorized_i2][0], 2) + math.pow(
                            categorized_list[categorized_i1][1] -
                            categorized_list[categorized_i2][1], 2))
    return result


#
# 単体テスト
#
import unittest


class Test(unittest.TestCase):

    def _generate_mock_board(self):
        board = Board(1)
        board.set_item(0, 0, 1)
        board.set_item(1, 1, 2)
        board.set_item(0, 2, 4)
        return board

    def test_init(self):
        board = Board(1)
        self.assertTrue(len(board.normalize()) == 9)

    def test_calc_score(self):
        board = self._generate_mock_board()
        self.assertEqual(calc_score(board), 3.3941125496954285)
