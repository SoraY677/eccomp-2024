"""
メイン関数
"""

from board import Board
from typing import List

def run(population_max:int, side_num:int=3) -> List[List[int]]:
    """実行

    Args:
        population_max (int): 母集団数
        side_num (int, optional): 辺のセクション数. Defaults to 3.

    Returns:
        list[list[int]]: 計算結果
    """
    population: list[Board] = [Board(side_num)] * population_max

    # Todo

    return [child.normalize() for child in population]

