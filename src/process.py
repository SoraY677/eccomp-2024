from util import logger
from config import get_api_key, get_submit_max


def exec(question_id):
    """実行

  Args:
      question_id (str): 問題ID
  """
    init(question_id)
    run(question_id)


def init(question_id):
    """初期化

  Args:
      question_id (str): 問題ID
  """
    logger.init()
    logger.info(f'Selected Question: {question_id}')


def run(question_id):
    """初期化

  Args:
      question_id (str): 問題ID
  """
    logger.info('[run]')

    api_key = get_api_key(question_id)
    submit_max = get_submit_max(question_id)

    for i in range(submit_max):
        pass
        # 解算出

        # 解提出
        # submit()
