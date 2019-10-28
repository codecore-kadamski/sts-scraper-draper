FROM pypy:3.6-7.2.0-slim-stretch

ENV PYTHONDONTWRITEBYTECODE=1

#RUN apt-get update && install -y

RUN apt-get update && \
    apt-get install --quiet --yes \ 
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1

RUN pip install pip==19.2.3 poetry==0.12.17
RUN poetry config settings.virtualenvs.create false

ENV PYTHONPATH=/app
ARG DEVELOP=false

RUN mkdir -p /app
WORKDIR /app

RUN ln -s /usr/local/bin/pypy3 /usr/local/bin/python

COPY ./pyproject.toml /app

RUN poetry install -n # `if [ "$DEVELOP" = "true" ]; then echo ''; else echo '--no-dev'; fi`

COPY . /app

RUN pip uninstall --yes poetry && rm pyproject.toml poetry.lock
