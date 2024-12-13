"""
設定ファイル
"""
from dotenv import load_dotenv
from enum import Enum
from typing import NamedTuple
import os
import datetime
from transmission.const import QuestionType

load_dotenv()

ECCOMP_API_KEY = os.getenv('ECCOMP_API_KEY')

SOLVE_SINGLE_PREFIX = "s"
SOLVE_MULTI_PREFIX = "m"


class QuestionConfigItem(NamedTuple):
    ID: str
    SUBMIT_MAX: int
    QUESTION_TYPE: QuestionType
    IS_MOCK: bool


QUESTION_MAP: dict = {
    ### 単目的
    # https://opthub.ai/ja/competitions/eccomp2024/single-objective-1
    f"{SOLVE_SINGLE_PREFIX}-1":
    QuestionConfigItem(ID=os.getenv('SINGLE_OBJECTIVE_1_API_KEY'),
                       SUBMIT_MAX=30000,
                       QUESTION_TYPE=QuestionType.SINGLE,
                       IS_MOCK=False),
    # https://opthub.ai/ja/competitions/eccomp2024/single-objective-2
    f"{SOLVE_SINGLE_PREFIX}-2":
    QuestionConfigItem(ID=os.getenv('SINGLE_OBJECTIVE_2_API_KEY'),
                       SUBMIT_MAX=30000,
                       QUESTION_TYPE=QuestionType.SINGLE,
                       IS_MOCK=False),
    # https://opthub.ai/ja/competitions/eccomp2024/single-objective-3
    f"{SOLVE_SINGLE_PREFIX}-3":
    QuestionConfigItem(ID=os.getenv('SINGLE_OBJECTIVE_3_API_KEY'),
                       SUBMIT_MAX=30000,
                       QUESTION_TYPE=QuestionType.SINGLE,
                       IS_MOCK=False),
    # mock
    f"{SOLVE_SINGLE_PREFIX}-x":
    QuestionConfigItem(ID="XXX",
                       SUBMIT_MAX=100,
                       QUESTION_TYPE=QuestionType.SINGLE,
                       IS_MOCK=True),
    ### 多目的
    # https://opthub.ai/ja/competitions/eccomp2024/multi-objective-1
    f"{SOLVE_MULTI_PREFIX}-1":
    QuestionConfigItem(ID=os.getenv('MULTI_OBJECTIVE_1_API_KEY'),
                       SUBMIT_MAX=10000,
                       QUESTION_TYPE=QuestionType.MULTI,
                       IS_MOCK=False),
    # https://opthub.ai/ja/competitions/eccomp2024/multi-objective-2
    f"{SOLVE_MULTI_PREFIX}-2":
    QuestionConfigItem(ID=os.getenv('MULTI_OBJECTIVE_2_API_KEY'),
                       SUBMIT_MAX=10000,
                       QUESTION_TYPE=QuestionType.MULTI,
                       IS_MOCK=False),
    # https://opthub.ai/ja/competitions/eccomp2024/multi-objective-3
    f"{SOLVE_MULTI_PREFIX}-3":
    QuestionConfigItem(ID=os.getenv('MULTI_OBJECTIVE_3_API_KEY'),
                       SUBMIT_MAX=10000,
                       QUESTION_TYPE=QuestionType.MULTI,
                       IS_MOCK=False),
    # mock
    f"{SOLVE_MULTI_PREFIX}-x":
    QuestionConfigItem(ID="XXX",
                       SUBMIT_MAX=100,
                       QUESTION_TYPE=QuestionType.MULTI,
                       IS_MOCK=True)
}


def get_question_config_item(question_id: str) -> QuestionConfigItem:
    """問題の設定情報取得

    Args:
        question_id (str): 問題ID

    Raises:
        None

    Returns:
        QuestionConfigItem: 設定情報
    """
    if question_id not in QUESTION_MAP:
        raise None

    return QUESTION_MAP[question_id]


POPULATION_MAX = 10  # 10個体
GENERATION_MAX = 100  # 100回進化
MUTATION_RATE = 0.05  # 突然変異率


def is_validate_question_id(question_id: str) -> bool:
    """問題IDの存在真偽判定

    Args:
        question_id (str): 問題ID

    Returns:
        bool
    """
    return question_id in QUESTION_MAP.keys()

def get_result_file_path(question_id):
    return f'./data/result-{question_id}-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv'

def get_log_file_path(question_id):
    return f'./log/{question_id}/log-{question_id}-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log'
