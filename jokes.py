import random
from dataclasses import dataclass
from util import from_csv_to_dict


@dataclass
class Joke:
    setup: str
    punchline: str


class JokeService():
    def __init__(self, filepath: str):
        self.filepath = filepath
        raw_jokes = from_csv_to_dict(filepath)
        self.jokes = [Joke(**joke) for joke in raw_jokes]

    def get_random_joke(self) -> Joke:
        return random.choice(self.jokes)
