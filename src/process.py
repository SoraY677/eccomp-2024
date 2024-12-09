from util import logger
from config import get_api_key, get_submit_max, POPULATION_MAX
import solution
import math 


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


def run(question_id: str) -> None:
    """初期化

  Args:
      question_id (str): 問題ID
  """
    logger.info('[run]')

    api_key = get_api_key(question_id)
    submit_max = get_submit_max(question_id)
    print(solution)

    for _ in range(math.floor(submit_max / POPULATION_MAX)):
        # 解算出
        result = solution.run(POPULATION_MAX)

        # 解提出
        # submit()
