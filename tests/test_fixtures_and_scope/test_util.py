from fixtures_and_scope.jokes import Joke
from fixtures_and_scope.util import from_csv_to_dict


def test_from_csv_to_dict_returns_a_list_of_dicts_with_single_joke_file(single_joke_csv_filepath: str, single_joke: Joke):
    jokes = from_csv_to_dict(single_joke_csv_filepath)
    assert jokes == [single_joke.__dict__]


def test_from_csv_to_dict_returns_a_list_of_dicts_with_multiple_joke_file(multiple_jokes_csv_filepath: str, jokes: list[Joke]):
    joke_dicts = from_csv_to_dict(multiple_jokes_csv_filepath)
    assert joke_dicts == [joke.__dict__ for joke in jokes]
