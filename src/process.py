from util import logger


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
      question_id (_type_): _description_
  """
    logger.init()
    logger.info(f'Selected Question: {question_id}')


def run(question_id):
    logger.info('[run]')
    logger.info('Todo')
