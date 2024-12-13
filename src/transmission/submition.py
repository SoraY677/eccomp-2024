"""
解提出
"""
from os import path
import sys
from const import QuestionType, get_mock_single_response, get_mock_mutli_response, MOCK_ERROR_RESPONSE
from data import write
import random
from typing import Union
from opthub_client.api import OptHub

if __name__ == "__main__":
    sys.path.append('..')
else:
    sys.path.append(path.join(path.dirname(__file__), '..'))
from util import logger

_api_key: Union[str, None] = None
_question_id: Union[str, None] = None
_submit_max = -1
_question_type: Union[QuestionType, None] = None
_is_mock = True
_data_file_path = ''


def init(api_key: str,
         question_id: str,
         submit_max: int,
         question_type: QuestionType,
         is_mock: bool,
         data_file_path: str = ''):
    """初期化

  Args:
      api_key (int): 問題ID
      submit_max (int): 提出最大回数
  """
    global _api_key
    _api_key = api_key
    global _question_id
    _question_id = question_id
    global _submit_max
    _submit_max = submit_max
    global _question_type
    _question_type = question_type
    global _is_mock
    _is_mock = is_mock
    global _data_file_path
    _data_file_path = data_file_path


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
    global _data_file_path

    if _is_inited(_question_id, _submit_max, _question_type) is False:
        error_message = "transmission not inited"
        logger.error(error_message)
        return MOCK_ERROR_RESPONSE

    result_map = {}
    for id in ans_dict:
        ans = ans_dict[id]
        result_map[id] = _exec_process(ans)
        if _data_file_path != '':
            write(_data_file_path, {
                "ans": ans_dict[id],
                "result": result_map[id]
            })
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


def _exec_process(ans: any):
    """送信コマンド実行

  Args:
      ans (any): 解答オブジェクト

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
        return get_mock_single_response()
    elif _question_type.value is QuestionType.MULTI.value:
        return get_mock_mutli_response()

    return MOCK_ERROR_RESPONSE


def _post_server(ans: any) -> dict:
    """サーバへの提出

    Args:
        ans (any): 解答

    Returns:
        dict: 結果
    """
    global _api_key
    global _question_id
    try:
        # 参考実装: https://opthub.notion.site/OptHub-API-e35cc47419054d6b8723180b27405c49
        with OptHub(_api_key) as api:
            opthub_match = api.match(_question_id)
            trial = opthub_match.submit(ans)
            eval = trial.wait_evaluation()

            if eval.feasible is False:
                return MOCK_ERROR_RESPONSE

            return {
                'objective':
                0.2 if eval.objective.scalar is not None else
                eval.objective.vector,
                'feasible':
                True
            }
    except Exception as e:
        logger.error(e)
        return MOCK_ERROR_RESPONSE


#
# 単体テスト
#
import unittest


class Test(unittest.TestCase):

    def _run_before_test(self):
        logger.init()
        init('xxx', 'xxx', 0, QuestionType.SINGLE, True)

    def test_init(self):
        self._run_before_test()
        self.assertTrue(_question_id == 'xxx')
        self.assertTrue(_submit_max == 0)
        self.assertTrue(_question_type.value == QuestionType.SINGLE.value)

    def test_mock_submit(self):
        self._run_before_test()
        result = submit({'test': {}})
        self.assertTrue(result['test']['feasible']
                        == get_mock_single_response()['feasible']
                        or result['test'] == MOCK_ERROR_RESPONSE)
