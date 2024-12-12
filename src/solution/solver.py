"""
メイン関数
"""

from board import Board
from typing import List
from evolution import init, crossover
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

def _select(optimization_pairs: List[OptimizationPair], num = 2) -> List[OptimizationPair]:
    total_score = 0
    for pairs in optimization_pairs:
        total_score += pairs.get_evaluation_point()
    
    weights = [total_score / pairs.get_evaluation_point() for pairs in optimization_pairs]
    return random.choices(optimization_pairs, k=num, weights=weights)


def run(population_max: int,
        generation_max: int,
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
        return [init(side_num) for _ in range(population_max)]

    generated_results: List[OptimizationPair] = [optimization_pair for optimization_pair in optimization_pairs]
    for _ in generation_max:
        for _ in population_max:
            selected_individual = _select(optimization_pairs)
            new_board = crossover(selected_individual[0].get_board(), selected_individual[1].get_board(), 3) # 仮置きで3点交叉
        
            sample_individual = _select(optimization_pairs, 1)[0]
            score = math.sqrt(math.pow(sample_individual.get_evaluation_point() - calc_score(new_board), 2))
            generated_results.append(OptimizationPair(sample_individual, score))
        generated_results = []
    return [result.get_board() for result in generated_results]
