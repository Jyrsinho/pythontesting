from pathlib import Path
import os

from util import from_csv_to_dict


def test_csv_to_dict_reads_rows_to_dictionary():
    tmp_test_file_path = '/tmp/test-data.csv'
    Path(tmp_test_file_path).parent.mkdir(exist_ok=True)

    with open(tmp_test_file_path, 'w') as file:
        file.write('name,age\n')
        file.write('Aaro,25\n')
        file.write('Eero,27\n')
        file.write('Iiro,24\n')

    try:
        data = from_csv_to_dict(tmp_test_file_path)

        assert data == [
            {'name': 'Aaro', 'age': '25'},
            {'name': 'Eero', 'age': '27'},
            {'name': 'Iiro', 'age': '24'}
        ]
    finally:
        os.remove(tmp_test_file_path)
