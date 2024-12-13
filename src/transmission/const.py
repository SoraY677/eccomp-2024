from enum import Enum
from random import random


class QuestionType(Enum):
    SINGLE = 1
    MULTI = 2


# カスタムレスポンス
def get_mock_single_response():
    return {'objective': random(), 'feasible': True}


def get_mock_mutli_response():
    return {'objective': [random(), random()], 'feasible': True}


MOCK_ERROR_RESPONSE = {'feasible': False}
