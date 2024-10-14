from fixtures_and_scope.jokes import JokeService 
from fixtures_and_scope.jokes import Joke


def test_get_random_joke_returns_the_only_joke(single_joke_csv_filepath: str, single_joke: Joke):
    joke_service = JokeService(single_joke_csv_filepath)
    joke = joke_service.get_random_joke()
    assert joke == single_joke


def test_get_random_joke_can_return_all_different_jokes(multiple_jokes_csv_filepath: str, jokes: list[Joke]):
    """
    This test is flaky in theory, but in practice, it should not fail in any reasonable number of test runs.

    Explanation:

    With three distinct values, the first sample will always be a new joke. The second sample will be a new one with a 
    probability of 2/3. The third sample will be new with a probability of either 1/3 or 2/3 depending on the outcome 
    of the second sample, the former being the more probable one.

    To make the problem easier, let's first look at only getting two out of the three jokes.
    With a mere 10 samples, the probability of not getting two out of three jokes is (1-2/3)^9 ≈ 0.00005 = 1/20 000 
    and with 20 samples, we already get the probability down to (1-2/3)^19 which is less than 1 000 000 000.

    Then, we need to get our final joke. Now, assuming a situation where we have already sampled two out of three jokes, 
    the probability of getting the last joke is 1/3. The probability of not getting the last joke in 10 samples is much
     higher this time; (1-1/3)^9 ≈ 0.026 ≈ 1/30, but with 50 samples, we are again at extremely low probabilities 
     (1-1/3)^49 ≈ 1.5 / 1 000 000 000.
    """

    # With a small number of jokes and high number of samples, the probability of not getting all jokes is near non-existent

    joke_service = JokeService(multiple_jokes_csv_filepath)

    # Some logic is unavoidable here, as we need to check that all available jokes are retrieved with enough samples
    iterations = 100 * len(jokes)

    random_jokes = [joke_service.get_random_joke() for _ in range(iterations)]

    distinct_jokes = []
    for random_joke in random_jokes:
        if random_joke not in distinct_jokes:
            distinct_jokes.append(random_joke)

    assert len(distinct_jokes) == len(jokes)
    assert all(
        random_joke in jokes for random_joke in distinct_jokes), f"Expecting all random jokes to be in {jokes}, got {distinct_jokes}"
