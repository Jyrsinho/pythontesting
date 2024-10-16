# build stage
FROM python:3.12-alpine as builder

WORKDIR /srv

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN pip install poetry==1.8.2

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

COPY . .

# runtime 
FROM python:3.12-alpine as runtime

WORKDIR /srv

ENV VIRTUAL_ENV=/srv/.venv \
    PATH="/srv/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --from=builder /srv /srv

CMD ["fastapi", "run", "main.py", "--port", "8000"]
