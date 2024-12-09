from util import logger
from config import get_api_key, get_submit_max
import solution


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

    for i in range(submit_max):
        pass
        # 解算出
        # result = solution.run()

        # print(result
        pass

        # 解提出
        # submit()
