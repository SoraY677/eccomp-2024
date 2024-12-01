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
        "api_key": os.getenv('SINGLE_OBJECTIVE_1_API_KEY'),
        "SUBMIT_MAX": 30000
    },
    # https://opthub.ai/ja/competitions/eccomp2024/single-objective-2
    f"{SOLVE_SINGLE_PREFIX}-2": {
        "api_key": os.getenv('SINGLE_OBJECTIVE_2_API_KEY'),
        "SUBMIT_MAX": 30000
    },
    # https://opthub.ai/ja/competitions/eccomp2024/single-objective-3
    f"{SOLVE_SINGLE_PREFIX}-3": {
        "api_key": os.getenv('SINGLE_OBJECTIVE_3_API_KEY'),
        "SUBMIT_MAX": 30000
    },
    ### 多目的
    # https://opthub.ai/ja/competitions/eccomp2024/multi-objective-1
    f"{SOLVE_MULTI_PREFIX}-1": {
        "api_key": os.getenv('MULTI_OBJECTIVE_1_API_KEY'),
        "submit_max": 10000
    },
    # https://opthub.ai/ja/competitions/eccomp2024/multi-objective-2
    f"{SOLVE_MULTI_PREFIX}-2": {
        "api_key": os.getenv('MULTI_OBJECTIVE_2_API_KEY'),
        "submit_max": 10000
    },
    # https://opthub.ai/ja/competitions/eccomp2024/multi-objective-3
    f"{SOLVE_MULTI_PREFIX}-3": {
        "api_key": os.getenv('MULTI_OBJECTIVE_3_API_KEY'),
        "submit_max": 10000
    }
}
