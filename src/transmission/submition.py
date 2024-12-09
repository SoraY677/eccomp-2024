"""
解提出
"""
from os import path
from enum import Enum
import sys
import json
import subprocess
from const import QuestionType, MOCK_SINGLE_RESPONSE, MOCK_MULTI_RESPONSE, MOCK_ERROR_RESPONSE
import random
from typing import Union

if __name__ != "__main__":
    sys.path.append(path.dirname(__file__))
else:
    sys.path.append('..')
from util import logger
from const import RESULT_STATUS_ERROR

_question_id: Union[str, None] = None
_submit_max = -1
_question_type: Union[QuestionType, None] = None
_is_mock = True


def init(question_id: str, submit_max: int, question_type: QuestionType,
         is_mock: bool):
    """初期化

  Args:
      api_key (int): 問題ID
      submit_max (int): 提出最大回数
  """
    global _question_id
    _question_id = question_id
    global _submit_max
    _submit_max = submit_max
    global _question_type
    _question_type = question_type
    global _is_mock
    _is_mock = is_mock


def submit(ans_dict: dict) -> dict:
    """解提出

  Args:
      ans_dict (dict): 解答群
      is_mock (bool): モックフラグ

  Returns:
      dict : 結果群
  """
    global _question_id
    global _submit_max
    global _question_type

    if _is_inited(_question_id, _submit_max, _question_type) is False:
        error_message = "transmission not inited"
        logger.error(error_message)
        return MOCK_ERROR_RESPONSE

    result_map = {}
    for id in ans_dict:
        ans = ans_dict[id]
        result_map[id] = _exec_process(ans)
    return result_map


def _is_inited(question_id, submit_max, question_type):
    """初期化確認

  Returns:
      bool: 初期化完了真偽
  """
    if question_id == None:
        return False
    elif submit_max == -1:
        return False
    elif question_type == None:
        return False
    return True


def _exec_process(ans: dict):
    """送信コマンド実行

  Args:
      ans (dict): 解答オブジェクト

  Returns:
      dict: 実行結果
  """
    global _is_mock
    if _is_mock:
        return _get_mock()

    return _post_server(ans)


def _get_mock() -> dict:
    """モックでの疑似回答提出

    Returns:
        dict: 結果
    """
    if random.random() < 0.2:
        return MOCK_ERROR_RESPONSE

    global _question_type
    if _question_type.value is QuestionType.SINGLE.value:
        return MOCK_SINGLE_RESPONSE
    elif _question_type.value is QuestionType.MULTI.value:
        return MOCK_MULTI_RESPONSE

    return MOCK_ERROR_RESPONSE


def _post_server(ans: dict) -> dict:
    """サーバへの提出

    Args:
        ans (dict): リクエスト内容

    Returns:
        dict: 結果
    """
    try:
        global _question_id
        command = f"echo {json.dumps(ans)} | opt submit --match={_question_id}"
        process = subprocess.Popen(command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   shell=True)
        return _decode_response(process.communicate()[0])
    except Exception as e:
        logger.error(e)
        return MOCK_ERROR_RESPONSE


def _decode_response(response_txt):
    """レスポンスのデコード

    Args:
        response_txt (string): レスポンス内容文字列 

    Returns:
        dict: レスポンス内容の辞書型
    """
    try:
        decoded_response = json.loads(response_txt)
        logger.info(f'response: {decoded_response}')
        return decoded_response
    except Exception as e:
        raise e


if __name__ == "__main__":
    import unittest

    #テストケース一覧(提出は実際にしてしまうため未検証)
    class Test(unittest.TestCase):

        def _run_before_test(self):
            logger.init()

        def test_init(self):
            self._run_before_test()
            init(0, 0)
            self.assertTrue(_question_id == 0)
            self.assertTrue(_submit_max == 0)

        def test_not_inited(self):
            self._run_before_test()
            init(-1, -1)
            result = submit({})
            self.assertTrue(result['status'] == RESULT_STATUS_ERROR)

        def test_inited_but_safe_mode_activate(self):
            self._run_before_test()
            init(0, 0)
            result = submit({})
            self.assertTrue(result['status'] == RESULT_STATUS_ERROR)

    unittest.main()
