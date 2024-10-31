FROM python:3.12

WORKDIR /good_habit

COPY pyproject.toml .

RUN pip install --upgrade pip

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-root

COPY . .
