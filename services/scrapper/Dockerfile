FROM pypy:3.6-7.2.0-slim-stretch

RUN pip install pip==19.2.3 poetry==0.12.17
RUN poetry config settings.virtualenvs.create false

ARG DEVELOP=false
ARG ENV_MODE=dev

RUN mkdir -p /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

RUN ln -s /usr/local/bin/pypy3 /usr/local/bin/python

COPY ./pyproject.toml /app

RUN poetry install -n # `if [ "$DEVELOP" = "true" ]; then echo ''; else echo '--no-dev'; fi`

COPY . /app

RUN pip uninstall --yes poetry && rm pyproject.toml poetry.lock
