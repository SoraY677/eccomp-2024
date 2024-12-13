import random
from typing import Union, List
from os import path
import sys
if __name__ == "__main__":
    sys.path.append('..')
else:
    sys.path.append(path.join(path.dirname(__file__), '..'))
from board import Board
from board_generator import custom_generate


def init(side_num: int, hint_pattern: List[int]) -> Union[Board, None]:
    """初期解生成

    Args:
        side_num (int): 列のセクション数

    Returns:
        Board: 生成した盤面
    """

    # 実行可能解が現れるまで無限生成
    while (True):
        hint_board = Board(side_num)
        if hint_board.get_item_max() != len(hint_pattern):
            raise ValueError('board item num not equals hint_pattern')
        get_empty_index = hint_board.get_empty_index()
        hint_pattern_index = [
            i for i, value in enumerate(hint_pattern) if value == 1
        ]
        for index in hint_pattern_index:
            row_i, column_i = get_empty_index[index]
            hint_board.set_item(row_i, column_i, 1)
        generated_table = custom_generate(hint_board.create_table())
        if generated_table is not None:
            break
    result = Board(side_num)
    result.reset_by_table(generated_table)
    return result


#
# 単体テスト
#
import unittest


class Test(unittest.TestCase):

    def test_init(self):
        board = init(3)
        self.assertTrue(len(board.normalize()) == 81)
