"""
メイン関数
"""

from board import Board
from typing import List
from evolution import init
import random
from optimizer import calc_score
import math


class OptimizationPair:
    _board: Board
    _evalution_point: float

    def __init__(self, board: Board, evalution_point: float):

        self._board = board
        self._evalution_point = evalution_point

    def get_board(self):
        return self._board

    def get_evaluation_point(self):
        return self._evalution_point


def _select(optimization_pairs: List[OptimizationPair],
            num=2) -> List[OptimizationPair]:
    """ルーレット選択方式

    Args:
        optimization_pairs (List[OptimizationPair]): 最適化用リスト
        num (int, optional): リストの要素数. Defaults to 2.

    Returns:
        List[OptimizationPair]: _description_
    """
    total_score = 0
    for pairs in optimization_pairs:
        total_score += pairs.get_evaluation_point()

    weights = [
        total_score / (pairs.get_evaluation_point()
                       if pairs.get_evaluation_point() != 0 else 1)
        for pairs in optimization_pairs
    ]
    if not any(weights):  # すべて0のパターンもあり得るので対応
        weights = [1] * len(optimization_pairs)
    return random.choices(optimization_pairs, k=num, weights=weights)


def run(population_max: int,
        generation_max: int,
        hint_pattern: List[int],
        optimization_pairs: List[OptimizationPair] = [],
        side_num: int = 3) -> List[Board]:
    """実行

    Args:
        population_max (int): 母集団数
        side_num (int, optional): 辺のセクション数. Defaults to 3.

    Returns:
        list[list[int]]: 計算結果
    """
    if len(optimization_pairs) <= population_max / 2:
        return [init(side_num, hint_pattern) for _ in range(population_max)]

    generated_results: List[OptimizationPair] = []
    for i in range(generation_max):
        for j in range(population_max):
            sample_individual = _select(optimization_pairs, 1)[0]
            new_board = init(side_num, hint_pattern)
            score = math.sqrt(
                math.pow(
                    sample_individual.get_evaluation_point() -
                    calc_score(new_board), 2))
            generated_results.append(OptimizationPair(new_board, score))
    results = []
    generated_results.sort(key=lambda result: result.get_evaluation_point())
    for result in generated_results[0:population_max]:
        results.append(result.get_board())
    return results
