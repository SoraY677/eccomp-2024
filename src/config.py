"""
設定ファイル
"""
from dotenv import load_dotenv
import os

load_dotenv()

ECCOMP_API_KEY = os.getenv('ECCOMP_API_KEY')

SOLVE_SINGLE_PREFIX = "s"
SOLVE_MULTI_PREFIX = "m"

QUESTION_MAP = {
    ### 単目的
    # https://opthub.ai/ja/competitions/eccomp2024/single-objective-1
    f"{SOLVE_SINGLE_PREFIX}-1": {
        "API_KEY": os.getenv('SINGLE_OBJECTIVE_1_API_KEY'),
        "SUBMIT_MAX": 30000
    },
    # https://opthub.ai/ja/competitions/eccomp2024/single-objective-2
    f"{SOLVE_SINGLE_PREFIX}-2": {
        "API_KEY": os.getenv('SINGLE_OBJECTIVE_2_API_KEY'),
        "SUBMIT_MAX": 30000
    },
    # https://opthub.ai/ja/competitions/eccomp2024/single-objective-3
    f"{SOLVE_SINGLE_PREFIX}-3": {
        "API_KEY": os.getenv('SINGLE_OBJECTIVE_3_API_KEY'),
        "SUBMIT_MAX": 30000
    },
    ### 多目的
    # https://opthub.ai/ja/competitions/eccomp2024/multi-objective-1
    f"{SOLVE_MULTI_PREFIX}-1": {
        "API_KEY": os.getenv('MULTI_OBJECTIVE_1_API_KEY'),
        "SUBMIT_MAX": 10000
    },
    # https://opthub.ai/ja/competitions/eccomp2024/multi-objective-2
    f"{SOLVE_MULTI_PREFIX}-2": {
        "API_KEY": os.getenv('MULTI_OBJECTIVE_2_API_KEY'),
        "SUBMIT_MAX": 10000
    },
    # https://opthub.ai/ja/competitions/eccomp2024/multi-objective-3
    f"{SOLVE_MULTI_PREFIX}-3": {
        "API_KEY": os.getenv('MULTI_OBJECTIVE_3_API_KEY'),
        "SUBMIT_MAX": 10000
    },
    # mock: single
    f"{SOLVE_SINGLE_PREFIX}-x": {
        "API_KEY": "xxx",
        "SUBMIT_MAX": 30000
    },
    # mock: single
    f"{SOLVE_MULTI_PREFIX}-x": {
        "API_KEY": "xxx",
        "SUBMIT_MAX": 10000
    }
}


def is_validate_question_id(question_id):
    """問題IDの存在真偽判定

    Args:
        question_id (str): 問題ID

    Returns:
        bool
    """
    return question_id in QUESTION_MAP.keys()


def get_api_key(question_id):
    """APIキー取得

    Args:
        question_id (str): 問題ID

    Raises:
        None
    
    Returns:
        str: apiキー
    """
    if question_id not in QUESTION_MAP:
        raise None

    return QUESTION_MAP[question_id]["API_KEY"]


def get_submit_max(question_id):
    """提出回数を取得

    Args:
        question_id (str): 問題ID
    
    Raises:
        None

    Returns:
        int: 提出回数
    """
    if question_id not in QUESTION_MAP:
        raise None

    return QUESTION_MAP[question_id]["SUBMIT_MAX"]
