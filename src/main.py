"""
実行エントリー用
- 引数受け取り
- process実行
"""
import sys
import process

from config import QUESTION_MAP

if __name__ == "__main__":
    args = sys.argv
    question_id = args[1]
    if question_id not in QUESTION_MAP.keys():
        print(f'{question_id} not in questions')
        sys.exit(1)

    process.exec(question_id)
