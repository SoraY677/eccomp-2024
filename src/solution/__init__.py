import sys
from os import path

sys.path.append(path.dirname(__file__))
from solver import run

__all__ = ["run"]
