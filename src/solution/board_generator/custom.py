import generator
from typing import List, Union
import numpy as np


def custom_generate(pattern: List[List[int]]) -> Union[List[List[int]], None]:
    try:
        if generator.generate(np.array(pattern)):
            return generator.getProblem().tolist()
    except Exception as e:
        (f"Error: {e}")
    return None
