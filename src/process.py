from util import logger
from typing import List
from config import POPULATION_MAX, GENERATION_MAX, get_question_config_item, get_log_file_path, get_result_file_path
import solution
import math
from transmission import submition
from solution import OptimizationPair
import logging


def exec(api_key: str, question_id: str) -> None:
    """実行

  Args:
      question_id (str): 問題ID
  """
    init(api_key, question_id)
    run(question_id)


def init(api_key: str, question_id: str) -> None:
    """初期化

  Args:
      question_id (str): 問題ID
  """
    logger.init(get_log_file_path(question_id), logging.INFO)
    logger.info(f'Selected Question: {question_id}')

    question_config_item = get_question_config_item(question_id)
    submition.init(api_key, question_config_item.ID,
                   question_config_item.SUBMIT_MAX,
                   question_config_item.QUESTION_TYPE,
                   question_config_item.IS_MOCK,
                   get_result_file_path(question_id))


def run(question_id: str) -> None:
    """初期化

  Args:
      question_id (str): 問題ID
  """
    logger.info('[run]')

    question_config_item = get_question_config_item(question_id)
    optimization_pairs: List[OptimizationPair] = []
    optimize_responses = []
    for i in range(math.floor(question_config_item.SUBMIT_MAX /
                              POPULATION_MAX)):

        logger.info(f"========[{i+1}]========")

        # 解算出
        result = solution.run(POPULATION_MAX, GENERATION_MAX,
                              question_config_item.HINT_PATTERN,
                              optimization_pairs)
        # 解提出
        request_obj = {}
        for i in range(len(result)):
            board = result[i]
            request_obj[i] = board.normalize()

        logger.info(request_obj)
        responses = submition.submit(request_obj)
        logger.info(responses)
        sorted_reponse = sorted(
            {
                k: v
                for k, v in responses.items()
                if v.get('feasible') and 'objective' in v
            }.items(),
            key=lambda x:
            (max(x[1]['objective'][0], x[1]['objective'][1])
             if type(x[1]['objective']) is list else x[1]['objective']),
            reverse=True if responses[0]['feasible']
            and type(responses[0]['objective']) is list else False)

        # 実際に評価が高いものに独自評価を紐づける
        optimization_pairs = []
        for response in sorted_reponse:
            index = response[0]
            optimization_pair = OptimizationPair(
                result[index], solution.calc_score(result[index]))
            optimization_pairs.append(optimization_pair)
            optimize_responses.append(optimization_pair)
        optimize_responses = optimize_responses[(
            len(optimize_responses) -
            POPULATION_MAX if len(optimize_responses) > POPULATION_MAX else 0
        ):len(optimize_responses)]
