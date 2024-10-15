import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app, Joke

client = TestClient(app)


# Mock data
mock_jokes = [
    Joke(id=1, setup="Why did the chicken cross the road?", punchline="To get to the other side."),
    Joke(id=2, setup="Why don't skeletons fight?", punchline="They don't have the guts.")
]


@patch('main.find_jokes', return_value=mock_jokes)  # Mock the find_jokes function
def test_should_return_random_joke(mock_find_jokes):
    response = client.get('/joke/random')
    assert response.status_code == 200

    joke = response.json()

    # Check that the joke contains the necessary fields
    assert 'id' in joke
    assert 'setup' in joke
    assert 'punchline' in joke

    # Check that the joke is one of the jokes in mock_jokes
    assert joke['id'] in [1, 2]
    assert any(j['setup'] == joke['setup'] and j['punchline'] == joke['punchline'] for j in [
        {"id": 1, "setup": "Why did the chicken cross the road?", "punchline": "To get to the other side."},
        {"id": 2, "setup": "Why don't skeletons fight?", "punchline": "They don't have the guts."}
    ])
    
def test_should_return_a_joke_with_given_id()

