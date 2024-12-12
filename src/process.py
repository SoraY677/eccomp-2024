from util import logger
from typing import List
from config import POPULATION_MAX, get_question_config_item
import solution
import math
from transmission import submition
from solution import OptimizationPair


def exec(question_id: str) -> None:
    """実行

  Args:
      question_id (str): 問題ID
  """
    init(question_id)
    run(question_id)


def init(question_id: str) -> None:
    """初期化

  Args:
      question_id (str): 問題ID
  """
    logger.init()
    logger.info(f'Selected Question: {question_id}')

    question_config_item = get_question_config_item(question_id)
    submition.init(question_config_item.ID, question_config_item.SUBMIT_MAX,
                   question_config_item.QUESTION_TYPE,
                   question_config_item.IS_MOCK)


def run(question_id: str) -> None:
    """初期化

  Args:
      question_id (str): 問題ID
  """
    logger.info('[run]')

    question_config_item = get_question_config_item(question_id)
    optimization_pairs: List[OptimizationPair] = []
    for i in range(math.floor(question_config_item.SUBMIT_MAX /
                              POPULATION_MAX)):
        
        logger.info(f"========[{i+1}]========")
        # 解算出
        result = solution.run(POPULATION_MAX, optimization_pairs)

        # 解提出
        request_obj = {}
        for i in range(len(result)):
            board = result[i]
            request_obj[i] = _generate_ans_dict(board.normalize())

        logger.info(request_obj)
        responses = submition.submit(request_obj)
        logger.info(responses)
        soreted_reponse = sorted(
            {k: v for k, v in responses.items() if v.get('feasible') and 'objective' in v}.items(),
            key=lambda x: x[1]['objective'], reverse=True
        )

        # 実際に評価が高いものに独自評価を紐づける
        optimization_pairs = []
        for response in soreted_reponse:
            index = response[0]
            optimization_pairs.append(OptimizationPair(
                result[index],
                solution.calc_score(result[index])
            ))


def _generate_ans_dict(array: List[int]) -> dict:
    """リクエスト用オブジェクト作成

    Args:
        array (list[int]): 解答

    Returns:
        dict: リクエスト用オブジェクト
    """
    return {"variable": array}
