import pytest
import os
import tempfile


@pytest.fixture(scope="session")
def test_jokes():
    return [
        {'id': 1, 'setup': 'Why did the scarecrow win an award?',
         'punchline': 'Because he was outstanding in his field'},
        {'id': 2, 'setup': 'How do you organize a space party?',
         'punchline': 'You planet'},
        {'id': 3, 'setup': 'Why did the physics teacher break up with the biology teacher?',
         'punchline': 'There was no chemistry'},
        {'id': 4, 'setup': 'Why was the math book sad?',
         'punchline': 'Because it had too many problems'},
        {'id': 5, 'setup': 'What did the janitor say when he jumped out of the closet?',
         'punchline': 'Supplies!'}
    ]


@pytest.fixture(scope="session", autouse=True)
def init_joke_csv(test_jokes):
    with tempfile.TemporaryDirectory() as tmp_test_dir:
        tmp_test_file_path = os.path.join(tmp_test_dir, 'test-data.csv')

        with open(tmp_test_file_path, 'w') as file:
            file.write('setup,punchline\n')
            for joke in test_jokes:
                file.write(f"{joke['setup']},{joke['punchline']}\n")

        os.environ['JOKE_CSV'] = tmp_test_file_path

        yield

        # the tempfile context manager handles temporary directory cleanup
        del os.environ['JOKE_CSV']