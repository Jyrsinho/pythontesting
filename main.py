import os
from functools import lru_cache
from random import randint
from fastapi import APIRouter, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from dataclasses import dataclass

from util import from_csv_to_dict


@lru_cache
def get_joke_csv_path():
    return os.getenv('JOKE_CSV', 'jokes.csv')


# Model
@dataclass
class Joke:
    id: int
    setup: str
    punchline: str


# Service functions
def find_jokes() -> list[Joke]:
    raw_jokes = from_csv_to_dict(get_joke_csv_path())
    return [Joke(id=i + 1, **joke) for i, joke in enumerate(raw_jokes)]


def find_joke(id: int) -> Joke:
    raw_jokes = from_csv_to_dict(get_joke_csv_path(), read_until=id)
    if id < 1 or id > len(raw_jokes):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No joke found with id {id}')

    return Joke(id=id, **raw_jokes[id - 1])


# Routes
router = APIRouter()


@router.get('/health')
async def health() -> JSONResponse:
    return JSONResponse(content={'status': 'ok'}, status_code=status.HTTP_200_OK)


@router.get('/joke/random')
async def random_joke() -> Joke:
    jokes = find_jokes()
    joke_id = randint(1, len(jokes))
    return jokes[joke_id - 1]


@router.get('/joke/all')
async def get_jokes() -> list[Joke]:
    return find_jokes()


@router.get('/joke/{id}')
async def get_joke(id: int) -> Joke:
    return find_joke(id)


# App
app = FastAPI()
app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['Authorization', 'Content-Type']
)
