RED := \u001b[0;31m
NC := \u001b[0m
GREEN := \u001b[0;32m
YELLOW := \u001b[1;33m

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
    match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
    if match:
        target, help = match.groups()
        print(f'${GREEN}{target :20s}${NC} ${YELLOW}{help}${NC}')
endef

export PRINT_HELP_PYSCRIPT


help:
	@-python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

migrations-prod:  ##  migracje produkcyjne w bazie postgres
	@-export ENVIRON="prod" && poetry run python manage.py drop_db && poetry run python manage.py create_db && poetry run python manage.py db upgrade

migrations-test: develop  ##  migracje testowe w sqlite
	@-rm data-test.db
	@-rm data.db
	@-export ENVIRON="test" && poetry run python manage.py create_db && poetry run python manage.py db upgrade

start-local-server:  ##  start local server
	@-pkill gunicorn
	@-poetry run gunicorn -c gunicorn_config wsgi

build:  ##  buduje obraz kontenera
	@-docker build -t "scrapper_domain:latest" .

run: ##  uruchamia  aplikacje w dokerze
	@-docker run -p 5000:5000 --name scrapper_domain --detach scrapper_domain:latest

start:  ##  start project in containers
	@-docker volume create --name=front-media-volume
	@-docker-compose up --build -d

stop:  ##  stop project
	@-docker-compose stop
	@-docker-compose down

stop-local:  ##  zatrzymuje kontener
	@-docker stop scrapper_domain
	@-docker rm scrapper_domain

develop:  ##  poetry install requirements
	@-poetry install -n

test: migrations-test  ##  uruchamiamy testy
	@-poetry run python manage.py test

shell:
	@-export ENVIRON="prod" && poetry run python manage.py shell

docker-rmi:  ##  usuwanie obrazów 
	@-docker rmi -f $$(docker images)

docker-rm:  ##  usuwanie kontenerów
	@-docker rm -f $$(docker ps -a -q)
