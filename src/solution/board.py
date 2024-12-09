from os import path
import itertools
from typing import List
from enum import IntEnum
import math
import sys
if __name__ == "__main__":
    sys.path.append('..')
else:
    sys.path.append(path.join(path.dirname(__file__), '..'))
from util import logger

SINGLE_SIDE_NUM = 3


class ITEM(IntEnum):
    UNKOWN = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


class Board:

    _side_num = 0
    _list = []

    def __init__(self, side_num: int = 0) -> None:
        """コンストラクタ

        Args:
            all_size (int): 全体の1辺
            single_size (int): 1ブロック内の1辺
        """
        self._side_num = side_num
        self._list = [[ITEM.UNKOWN] * self._side_num * SINGLE_SIDE_NUM
                      for _ in range(self._side_num * SINGLE_SIDE_NUM)]

    def reset_by_normalized_list(self, normalized_list: List[int]) -> None:
        """１次元配列から盤面を再生成

        Args:
            normalized_list (List[int]): １次元配列
        """
        result = []
        column_max = math.floor(
            len(normalized_list) / (SINGLE_SIDE_NUM * self._side_num))
        for column_i in range(column_max):
            row = []
            for row_item in normalized_list[SINGLE_SIDE_NUM * self._side_num *
                                            column_i:SINGLE_SIDE_NUM *
                                            self._side_num * (column_i + 1)]:
                row.append(ITEM(row_item))
            result.append(row)
        self._list = result

    def _is_index_validation(self, row_i: int, column_i: int) -> bool:
        """テーブルのインデックス指定時のバリデーション

        Args:
            row_i (int)
            column_i (int)

        Returns:
            bool: バリデーション成功/失敗
        """
        if row_i >= len(self._list):
            logger.error('row index over size')
            return False
        elif column_i >= len(self._list):
            logger.error('row index over size')
            return False
        return True

    def _is_value_set_validation(self, row_i: int, column_i: int) -> bool:
        """値設定

        Args:
            row_i (int)
            column_i (int)

        Returns:
            bool: 値が設定できるか検証
        """
        if ITEM.ONE <= self._list[column_i][row_i] <= ITEM.NINE:
            logger.error(
                f'value is over range:{self._list[column_i][row_i]}([{row_i}][{column_i}])'
            )
            return False
        return True

    def set_item(self, row_i: int, column_i: int, value: int) -> None:
        """盤面の指定箇所に数値設定

        Args:
            row_i (int)
            column_i (int)
            value (ITEM): 設定値

        Raises:
            None
        """
        if self._is_index_validation(
                row_i, column_i) is False or self._is_value_set_validation(
                    row_i, column_i) is False:
            raise None
        self._list[column_i][row_i] = value

    def get_empty_index(self) -> List[List[int]]:
        """まだ値が確定していないインデックス(行・列)リストを取得

        Returns:
            list: [行,列]要素からなる2次元配列
        """
        result = []
        for column_i in range(len(self._list)):
            for row_i in range(len(self._list[column_i])):
                if self._list[column_i][row_i] == ITEM.UNKOWN:
                    result.append([row_i, column_i])
        return result

    def get_setable_item_value(self, row_i: int, column_i: int) -> List[ITEM]:
        """指定の箇所において設定できる値リストを取得

        Args:
            row_i (int)
            column_i (int)

        Returns:
            list: 設定できる値リスト 
        """
        result = [
            item for item in ITEM if ITEM.ONE <= item.value <= ITEM.NINE
            and item.value != ITEM.UNKOWN
        ]

        side_num = len(self._list)

        # 同じ列で同数字があるといけないので除く
        for search_i in range(side_num):
            if self._list[column_i][search_i] in result:
                result.remove(self._list[column_i][search_i])

        # 同じ行で同数字があるといけないので除く
        for search_i in range(side_num):
            if self._list[search_i][row_i] in result:
                result.remove(self._list[search_i][row_i])

        # 同じブロック内に同数字があるといけないので除く
        for block_column_i in range(SINGLE_SIDE_NUM):
            for block_row_i in range(SINGLE_SIDE_NUM):
                search_column_i = math.floor(
                    column_i / SINGLE_SIDE_NUM) + block_column_i
                search_row_i = math.floor(
                    row_i / SINGLE_SIDE_NUM) + block_row_i
                if self._list[search_column_i][search_row_i] in result:
                    result.remove(self._list[search_column_i][search_row_i])

        return result

    def normalize(self):
        """1次元配列化
        Returns:
            list: 1次元配列に変更したもの
        """
        return [
            item.value
            for item in list(itertools.chain.from_iterable(self._list))
        ]

    def get_item_max(self) -> int:
        """マス数を取得

        Returns:
            int: マス合計数
        """
        return len(
            self._list) * (len(self._list[0]) if len(self._list) > 0 else 0)

    def get_side_num(self) -> int:
        """列のセクション数を取得

        Returns:
            int: 列のセクション数
        """
        return self._side_num


import unittest


#テストケース一覧(提出は実際にしてしまうため未検証)
class Test(unittest.TestCase):

    _board = Board(3)

    def _run_before_test(self):
        logger.init()
        self._board = Board(3)

    def test_standard_init(self):
        self._run_before_test()
        self.assertTrue(self._board.normalize() == [0] * 81)

    def test_set_item(self):
        self._run_before_test()
        self._board.set_item(1, 1, ITEM.TWO)
        compared = [ITEM.UNKOWN] * 81
        compared[10] = ITEM.TWO
        self.assertTrue(self._board.normalize() == compared)

    def test_reset_by_normalized_list(self):
        self._run_before_test()
        self._board.reset_by_normalized_list([0] * 81)
        self.assertTrue(self._board.normalize() == [0] * 81)

    def test_get_setable_item_value(self):
        self._run_before_test()
        self._board.set_item(0, 0, ITEM.ONE)
        self._board.set_item(0, 1, ITEM.EIGHT)
        self._board.set_item(0, 2, ITEM.FIVE)
        self._board.set_item(1, 0, ITEM.TWO)
        self._board.set_item(1, 1, ITEM.THREE)
        self._board.set_item(1, 2, ITEM.FOUR)
        self._board.set_item(2, 1, ITEM.SIX)
        self.assertTrue(
            self._board.get_setable_item_value(2, 0) ==
            [ITEM.SEVEN, ITEM.NINE])

    def test_normalize(self):
        self._run_before_test()
        self.assertTrue(self._board.normalize() == [0] * 81)
