import pytest
from starlette.templating import pass_context


@pytest.fixture(scope='session')
def single_joke_csv_filepath(tmp_path):
    #a fixture that returns the path to a temporary csv file containing a single joke 
    # (the fixture may create the file or the file can be created in another fixture)
    
    temp_file = tmp_path / 'temp_file.csv'
    
    temp_file.write_text("Apple is designing a new automatic car., But they're having trouble installing Windows!")
    
    return temp_file.absolute()


@pytest.fixture(scope='session')
def single_joke(single_joke_csv_filepath):
    return str(single_joke_csv_filepath)