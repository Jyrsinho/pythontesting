# Simple joke api

Just a simple joke api that returns jokes in the format

```json
{
    "id": 1
    "setup": "What do you call a bear with no teeth?",
    "punchline": "A gummy bear"
}
```

## Usage

- GET request to `/joke/random` returns a random joke
- GET request to `/joke/all` returns all available jokes
- GET request to `/joke/{id}` returns a joke with the specified id (replace `{id}` with the id of the joke you want to get)

## Requirements

Running the application requires either [Poetry](https://python-poetry.org/) or [Docker](https://www.docker.com/).

## Installation and setup

- Clone the repository
- Go to the project directory

### With Poetry

- Run `poetry install` to install the dependencies
- Run `poetry run uvicorn main:app --port 9000 --reload` to start the server on port 9000

### With Docker

- Run `./build.sh` to build the docker image
- Run `./run.sh [port]` to run the docker container on port 9000 by default (no arguments) or on the port specified by the optional argument.

The run script will make the server run on the background.
To stop the server, run `./stop.sh`.

## Testing

Testing is done with pytest. Prior to running the tests, make sure the dependencies are installed.

Options to run tests with Poetry:

1. Run `poetry run pytest` to run the tests
2. Run `poetry shell` to activate the virtual environment and then run `pytest`
