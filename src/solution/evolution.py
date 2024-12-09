import random
from os import path
import sys
if __name__ != "__main__":
    sys.path.append(path.dirname(__file__))
else:
    sys.path.append('..')
from board import Board

def init(side_num: int) -> Board:
    """初期解生成

    Args:
        side_num (int): 列のセクション数

    Returns:
        Board: 生成した盤面
    """
    result = Board(side_num)
    empty_indexes = result.get_empty_index()
    hint_max_num = random.randint(0, result.get_item_max()) # Todo: 後でヒント数の最小は調整してもいいかも
    for _ in range(hint_max_num):
        selected_index = random.randint(0, len(empty_indexes)-1)
        row_i, column_i = empty_indexes.pop(selected_index)
        setable_nums = result.get_setable_item_value(row_i, column_i) # Todo: 0になるパターンがあるため考えてもいいかも
        if len(setable_nums) > 0:
            item = setable_nums[random.randint(0, len(setable_nums)-1)]
            result.set_item(row_i, column_i, item)
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
        index = random.randint(0, len(selectable_cross_point_list)-1)
        cross_point_index_list.append(selectable_cross_point_list.pop(index))
    cross_point_index_list = sorted(cross_point_index_list)

    result = [v for v in normalized_board_1]
    current_normalized_board_num = 2
    current_normalized_board = normalized_board_2
    for point_i in range(len(cross_point_index_list)):
        if point_i == 0:
            continue
        prev_point = cross_point_index_list[point_i-1]
        current_point = cross_point_index_list[point_i]

        result[prev_point:current_point] = current_normalized_board[prev_point:current_point]
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

if __name__ == "__main__":
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
    unittest.main()
