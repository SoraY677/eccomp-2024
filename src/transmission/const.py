from enum import Enum
from random import random


class QuestionType(Enum):
    SINGLE = 1
    MULTI = 2


# カスタムレスポンス
MOCK_SINGLE_RESPONSE = {'objective': random(), 'feasible': True}
MOCK_MULTI_RESPONSE = {'objective': [random(), random()], 'feasible': True}
MOCK_ERROR_RESPONSE = {'feasible': False}
