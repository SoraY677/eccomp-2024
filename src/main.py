"""
実行エントリー用
- 引数受け取り
- process実行
"""
import sys
import process

from config import is_validate_question_id

if __name__ == "__main__":
    args = sys.argv
    question_id = args[1]
    if is_validate_question_id(question_id) == False:
        print(f'{question_id} not in questions')
        sys.exit(1)

    process.exec(question_id)
