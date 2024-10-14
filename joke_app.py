from time import sleep
from jokes import JokeService


if __name__ == "__main__":
    joke_service = JokeService("jokes.csv")
    joke = joke_service.get_random_joke()

    print(joke.setup)
    sleep(2)
    print(joke.punchline)
