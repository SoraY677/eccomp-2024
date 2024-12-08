"""
メイン関数
"""

from board import Board


def run(population_max, side_num=3):
    population = [Board(side_num)] * population_max
