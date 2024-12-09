from enum import Enum

RESULT_STATUS_ERROR = "error"

MOCK_SINGLE_RESPONSE = {'objective': 0.5672, 'feasible': True}
MOCK_MULTI_RESPONSE = {'objective': [0.3154, 0.3619], 'feasible': True}
MOCK_ERROR_RESPONSE = {'feasible': False}


class QuestionType(Enum):
    SINGLE = 1
    MULTI = 2
