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
        if setable_nums > 0:
            item = setable_nums[random.randint(0, len(setable_nums)-1)]
            result.set_item(row_i, column_i, item)
    return result

def crossover(board_1: Board, board_2: Board, crossover_point_num: int):
    pass

def mutate():
    pass

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        
        def test_init(self):
            self._board = init(3)
            print(self._board.normalize())
            self.assertTrue(len(self._board.normalize()) == 81)
    unittest.main()
