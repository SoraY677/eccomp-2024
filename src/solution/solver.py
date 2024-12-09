"""
メイン関数
"""

from board import Board
from typing import List
from evolution import init


class OptimizationPair:
    _board: Board
    _evalution_point: float

    def __init__(self, board: Board, evalution_point: float):

        self._board = board
        self._evalution_point = evalution_point


def run(population_max: int,
        optimization_pairs: List[OptimizationPair] = [],
        side_num: int = 3) -> List[Board]:
    """実行

    Args:
        population_max (int): 母集団数
        side_num (int, optional): 辺のセクション数. Defaults to 3.

    Returns:
        list[list[int]]: 計算結果
    """

    if len(optimization_pairs) == 0:
        return [init(side_num) for _ in range(population_max)]

    return []  # Todo
