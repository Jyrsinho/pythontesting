from multiprocessing.pool import ApplyResult

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient


#/joke/random - returns a random joke
def test_random_should_return_a_random_joke():
    # For the /joke/random endpoint, it is enough to check that the server returns a joke in the correct format. 
    response = client.get('/joke/random')
    assert response.status_code == 200
    
    
    

#/joke/{id} - returns a joke with the given id
#/joke/all - returns a list of all jokes
