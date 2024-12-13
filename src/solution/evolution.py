import random
from typing import Union
from os import path
import sys
if __name__ == "__main__":
    sys.path.append('..')
else:
    sys.path.append(path.join(path.dirname(__file__), '..'))
from board import Board
from board_generator import custom_generate


def init(side_num: int) -> Union[Board, None]:
    """初期解生成

    Args:
        side_num (int): 列のセクション数

    Returns:
        Board: 生成した盤面
    """

    # 実行可能解が現れるまで無限生成
    while(True):
        hint_board = Board(side_num)
        hint_max_num = random.randint(0, hint_board.get_item_max())
        empty_indexes = hint_board.get_empty_index()
        for _ in range(hint_max_num):
            selected_index = random.randint(0, len(empty_indexes) - 1)
            row_i, column_i = empty_indexes.pop(selected_index)
            hint_board.set_item(row_i, column_i, 1)
        generated_table = custom_generate(hint_board.create_table())
        if generated_table is not None:
            break
    result = Board(side_num)
    result.reset_by_table(generated_table)
    return result


def crossover(board_1: Board, board_2: Board, crossover_point_num: int):
    """交叉

    Args:
        board_1 (Board): 交叉親盤面
        board_2 (Board): 交叉子盤面
        crossover_point_num (int): 交叉点数

    Returns:
        Board: 生成した盤面
    """
    normalized_board_1 = board_1.normalize()
    normalized_board_2 = board_2.normalize()

    # 交叉点をランダム生成
    selectable_cross_point_list = list(range(crossover_point_num))
    cross_point_index_list = []
    for _ in range(crossover_point_num):
        index = random.randint(0, len(selectable_cross_point_list) - 1)
        cross_point_index_list.append(selectable_cross_point_list.pop(index))
    cross_point_index_list = sorted(cross_point_index_list)

    result = [v for v in normalized_board_1]
    current_normalized_board_num = 2
    current_normalized_board = normalized_board_2
    for point_i in range(len(cross_point_index_list)):
        if point_i == 0:
            continue
        prev_point = cross_point_index_list[point_i - 1]
        current_point = cross_point_index_list[point_i]

        result[prev_point:current_point] = current_normalized_board[
            prev_point:current_point]
        current_normalized_board = normalized_board_1 if current_normalized_board_num == 2 else normalized_board_2

    new_board = Board(board_1.get_side_num())
    new_board.reset_by_normalized_list(result)
    return new_board


def mutate(side_num: int) -> Board:
    """突然変異

    Args:
        side_num (int): 列のセクション数

    Returns:
        Board: 生成した盤面
    """
    return init(side_num)


#
# 単体テスト
#
import unittest


class Test(unittest.TestCase):

    def test_init(self):
        board = init(3)
        self.assertTrue(len(board.normalize()) == 81)

    def test_crossover(self):
        board = init(3)
        board_2 = init(3)
        result = crossover(board, board_2, 3)
        self.assertTrue(len(result.normalize()) == 81)
