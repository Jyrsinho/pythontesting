import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app, Joke

client = TestClient(app)

@patch('main.find_jokes')  # Mock the find_jokes function
def test_should_return_random_joke(mock_find_jokes, test_jokes):
    # Mock the find_jokes function to return the test_jokes fixture
    mock_find_jokes.return_value = test_jokes

    response = client.get('/joke/random')
    assert response.status_code == 200

    joke = response.json()

    # Tarkistetaan, että vitsillä on oikeat kentät.
    assert 'id' in joke
    assert 'setup' in joke
    assert 'punchline' in joke

    # Tarkistetaan, että vitsi on yksi testvitseistä
    assert joke['id'] in [j['id'] for j in test_jokes]
    assert any(j['setup'] == joke['setup'] and j['punchline'] == joke['punchline'] for j in test_jokes)
    print(joke)


#/joke/{id} - returns a joke with the given id
@patch('main.find_jokes')
def test_should_return_joke_with_given_id(mock_find_jokes, test_jokes):
    mock_find_jokes.return_value = test_jokes
    
    response = client.get('/joke/2')
    assert response.status_code == 200
    
    joke = response.json()
    
    #Tarkistetaan, että tuli oikea vitsi
    assert joke['id'] == 2
    assert joke['setup'] == 'How do you organize a space party?'
    assert joke['punchline'] == 'You planet'
    
#
@patch('main.find_jokes')
def test_should_return_a_list_of_jokes(mock_find_jokes, test_jokes):
    mock_find_jokes.return_value = test_jokes
    
    response = client.get('/joke/all')
    assert response.status_code == 200
    
    jokes = response.json()
    
    assert jokes == test_jokes
    
