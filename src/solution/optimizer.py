from enum import Enum
from typing import Tuple
import math

from board import Board

class LineType(Enum):
    VERTICAL = 0
    HORIZONTAL = 1
    LEFT_TOP_DIAGONAL = 2
    RIGHT_TOP_DIAGONAL = 3
    POINT = 4

def _calc_next_search_from_end_index(
    line_num: int,
    search_index: Tuple[int],
    search_direction: Tuple[int],
    move_direction_over: Tuple[int]
) -> Tuple[int]:
    """対象位置の探索インデックス算出

    Args:
        line_num (int): 1辺のマス数
        search_index (Tuple[int]): 現在の探索(x,y)
        search_direction (Tuple[int]): 探索方向(x,y)
        move_direction_over (Tuple[int]): 探索時にマスを超えた際の移動方向(x,y)

    Returns:
         Tuple[int]: 次探索対象のインデックス
    """
    search_x = search_index[0] + search_direction[0]
    search_y = search_index[1] + search_direction[1]
    if search_x >= line_num:
        search_y += move_direction_over[1]
        search_x = 0
    elif search_x < 0:
        search_y += move_direction_over[1]
        search_x = line_num - 1
    elif search_y >= line_num:
        search_y = 0
        search_x += move_direction_over[0]
    elif search_y < 0:
        search_y = line_num - 1
        search_x += move_direction_over[0]

    return (search_x, search_y)

def _search_and_calc_evalutaion_point(
    board: Board,
    search_from_end_index: Tuple[int],
    search_direction_from_end: Tuple[int],
):
    """盤上を探索し、点数を算出

    Args:
        board (Board): 盤情報
        search_from_end_index (Tuple[int]): 対象位置の開始位置
        search_direction_from_end (Tuple[int]): 対象位置の進行方向

    Returns:
        _type_: _description_
    """
    
    line_num = board.get_size()
    current_search_from_start_index = (0, 0)
    current_search_from_end_index = search_from_end_index
    result = 0
    for _ in range(line_num * line_num ):
        # 2点間の相違があるか調査し、差があればマンハッタン距離を加算
        has_item_from_start = board.has_item(current_search_from_start_index[0], current_search_from_start_index[1])
        has_item_from_end = board.has_item(current_search_from_end_index[0], current_search_from_end_index[1])
        if has_item_from_start is not has_item_from_end:
            result += math.sqrt(math.pow(current_search_from_start_index[0] - round((line_num - 1) / 2), 2) + math.pow(current_search_from_start_index[1] - round((line_num - 1) / 2), 2))
        current_search_from_start_index = (current_search_from_start_index[0] + 1, current_search_from_start_index[1]) if current_search_from_start_index[0] + 1 < line_num else (0, current_search_from_start_index[1] + 1) 
        current_search_from_end_index = _calc_next_search_from_end_index(
            line_num,
            current_search_from_end_index,
            search_direction_from_end,
            (1 if current_search_from_end_index[0] == 0 else -1, 1 if current_search_from_end_index[1] == 0 else -1)
        )
    return result


def calc_symmetry_evalutaion_point(board: Board, line_type: LineType) -> float:
    """1対称での評価点算出

    Args:
        board (Board): 盤情報
        line_type (LineType): 対称の種類

    Returns:
        float: 点数
    """
    line_num = board.get_size()

    if line_type == LineType.VERTICAL:
        return _search_and_calc_evalutaion_point(
            board = board,
            search_from_end_index = (line_num - 1, 0),
            search_direction_from_end = (-1, 0),
        )
    elif line_type == LineType.HORIZONTAL:
        return _search_and_calc_evalutaion_point(
            board = board,
            search_from_end_index = (0, line_num - 1),
            search_direction_from_end = (1, 0)
        )
    elif line_type == LineType.LEFT_TOP_DIAGONAL:
        return _search_and_calc_evalutaion_point(
            board = board,
            search_from_end_index = (0, 0),
            search_direction_from_end = (0, 1)
        )
    elif line_type == LineType.RIGHT_TOP_DIAGONAL:
        return _search_and_calc_evalutaion_point(
            board = board,
            search_from_end_index = (line_num - 1, line_num - 1),
            search_direction_from_end = (0, -1)
        )
    elif line_type == LineType.POINT:
        return _search_and_calc_evalutaion_point(
            board = board,
            search_from_end_index = (line_num - 1, line_num - 1),
            search_direction_from_end = (-1, 0)
        )

    return -1.0

def calc_avg_evaluate(board: Board) -> float:
    """平均評価点を算出

    Args:
        board (Board): 盤情報

    Returns:
        float: 算出結果
    """
    result = 0.0
    for type in LineType:
        result += calc_symmetry_evalutaion_point(board, type)
    return result / 5

#
# 単体テスト
#
import unittest

class Test(unittest.TestCase):

    def _generate_mock_board(self):
        board = Board(1)
        board.set_item(0,0,1)
        board.set_item(1,1,2)
        board.set_item(0,2,4)
        return board

    def test_init(self):
        board = Board(1)
        self.assertTrue(len(board.normalize()) == 9)

    def test_calc_vertical_symmetry_evalutaion_point(self):
        board = self._generate_mock_board()
        self.assertEqual(calc_symmetry_evalutaion_point(board, LineType.VERTICAL), 5.6568542494923806)

    def test_calc_horizontal_symmetry_evalutaion_point(self):
            board = self._generate_mock_board()
            self.assertEqual(calc_symmetry_evalutaion_point(board, LineType.HORIZONTAL), 0)

    def test_calc_left_top_diagonal_symmetry_evalutaion_point(self):
        board = self._generate_mock_board()
        self.assertEqual(calc_symmetry_evalutaion_point(board, LineType.LEFT_TOP_DIAGONAL), 2.8284271247461903)

    def test_calc_right_top_diagonal_symmetry_evalutaion_point(self):
        board = self._generate_mock_board()
        self.assertEqual(calc_symmetry_evalutaion_point(board, LineType.RIGHT_TOP_DIAGONAL), 2.8284271247461903)

    def test_calc_point_symmetry_evalutaion_point(self):
        board = self._generate_mock_board()
        self.assertEqual(calc_symmetry_evalutaion_point(board, LineType.POINT), 5.6568542494923806)

    def test_calc_avg_evaluate(self):
        board = self._generate_mock_board()
        self.assertEqual(calc_avg_evaluate(board), 3.3941125496954285)
