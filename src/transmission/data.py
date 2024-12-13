import os
import csv
import unittest

def write(file_path: str, content: dict):
    """ファイルに結果を記載

    Args:
        file_path (str): _description_
        content (dict): _description_
    """
    if os.path.isfile(file_path):
        _write_add(file_path, content)
    else:
        _write_new(file_path, content)

def _write_new(file_path: str, content: dict):
    """ファイル新規作成

    Args:
        file_path (str): ファイルパス
        content (dict): 記載内容
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([list(content.keys()), list(content.values())])

def _write_add(file_path: str, content: dict):
    """ファイル追記

    Args:
        file_path (str): ファイルパス
        content (dict): 記載内容
    """
    # ヘッダーの整合性検証
    isHeaderValidation = False
    with open(file_path) as f:
        isHeaderValidation =  f.readline().replace('\n', '').split(',') == list(content.keys())
    if isHeaderValidation is False:
        raise ValueError('Submition data header is wrong')
    
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([list(content.values())])

import datetime
class Test(unittest.TestCase):

    _file_path = f'./test/transmission-data-test-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv'

    def test_first_write(self):
        write(self._file_path, {"id": 1, "value": "test"})
        self.assertTrue(os.path.isfile(self._file_path))
        with open(self._file_path) as f:
            self.assertEqual(f.read(), 'id,value\n1,test\n')
        os.remove(self._file_path)

    def test_second_write(self):
        write(self._file_path, {"id": 1, "value": "test"})
        self.assertTrue(os.path.isfile(self._file_path))
        write(self._file_path, {"id": 2, "value": "test2"})
        with open(self._file_path) as f:
            self.assertEqual(f.read(), 'id,value\n1,test\n2,test2\n')
        os.remove(self._file_path)
