"""
解提出
"""
from os import path
import sys
import json
import subprocess

if __name__ != "__main__":
    sys.path.append(path.dirname(__file__))
else:
    sys.path.append('..')
from util import logger
from const import RESULT_STATUS_ERROR

_match_num = -1
_submit_max = -1


def init(match_num, submit_max):
    """初期化

  Args:
      match_num (int): 問題番号
      submit_max (int): 提出最大回数
  """
    global _match_num
    _match_num = match_num
    global _submit_max
    _submit_max = submit_max


def submit(ans_dict, is_safe_mode=True):
    """解提出

  Args:
      ans_dict (dict): 解答群
      is_safe_mode (bool, optional): セーフモード. Defaults to True.

  Returns:
      dict : 結果群
  """
    global _match_num
    global _submit_max

    if _is_inited(_match_num, _submit_max) is False:
        error_message = "transmission not inited"
        logger.error(error_message)
        return _create_custom_error_dict(error_message)
    if is_safe_mode is True:
        error_message = 'Safe mode is activated'
        logger.error(error_message)
        return _create_custom_error_dict(error_message)

    result_map = {}
    for id in ans_dict:
        ans = ans_dict[id]
        result_map[id] = _exec_process(ans)
    return result_map


def _is_inited(_match_num, _submit_max):
    """初期化確認

  Returns:
      bool: 初期化完了真偽
  """
    if _match_num == -1:
        return False
    elif _submit_max == -1:
        return False
    return True


def _exec_process(ans):
    """送信コマンド実行

  Args:
      ans (obj): 解答オブジェクト

  Returns:
      dict: 実行結果
  """
    global _match_num
    global _submit_max

    try:
        command = f"echo {json.dumps(ans)} | opt submit --match={_match_num}"
        process = subprocess.Popen(command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   shell=True)
        return _decode_response(process.communicate()[0])
    except Exception as e:
        logger.error(e)
        return _create_custom_error_dict(e.__str__)


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


def _create_custom_error_dict(error_message):
    """解送信エラー時のレスポンスを自己定義

  Args:
      error_message (str): エラーメッセージ

  Returns:
      dict: 自作エラーリザルト
  """
    return {"message": error_message, "status": RESULT_STATUS_ERROR}


if __name__ == "__main__":
    import unittest

    #テストケース一覧(提出は実際にしてしまうため未検証)
    class Test(unittest.TestCase):

        def _run_before_test(self):
            logger.init()

        def test_init(self):
            self._run_before_test()
            init(0, 0)
            self.assertTrue(_match_num == 0)
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
