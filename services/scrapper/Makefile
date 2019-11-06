SHELL := /bin/bash
PWD := $(shell pwd)
WORKON_HOME := "$(dirname $(poetry run which python))"
APP_PATH := $(PWD)
APP := scrapper

RED := \u001b[0;31m
NC := \u001b[0m
GREEN := \u001b[0;32m
YELLOW := \u001b[1;33m`

.PHONY: docs
export PATH := $(WORKON_HOME)/bin:$(PATH)
export PYTHONPATH := "$(dirname $(poetry run which python))"
export ENV_PATH := "$(dirname $(poetry run which python))"

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

export DRIVERS_PATH := $(subst services/scrapper,drivers,$(APP_PATH))

help:
	@-python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

test:  ##  uruchamia testy unitest
	@-poetry run python -m unittest

run:  ##  run poetry
	@-poetry run python scrapper/run.py 2>&1 /dev/null || true

runs:  ##  runs poetry
	@-poetry run python scrapper/run_sync.py

clear:
	@-find . -name "__pycache__" -exec rm -rf {} \; 2>/dev/null || true
	@-find . -name "*.pyc" -exec rm -rf {} \; 2>/dev/null || true
	@-find . -name ".pytest_cache" -exec rm -rf {} \; 2>/dev/null || true
	@-find ../../ -name "pip-wheel-metadata" -exec rm -rf "{}" \; 2>/dev/null || true

install: clear  ##  install poetry
	@-poetry install

update: clear  ##  update poetry
	@-poetry update

develop:  ##  poetry install requirements
	@-poetry install  -n && poetry update

build:  ##  build image
	@-docker build -t $(APP) -f Dockerfile .

docker-run:  ##  run docker container
# 	@echo "$(DRIVERS_PATH)"
	@-docker run -d -it \
	--rm \
	--name $(APP) \
	--mount type=bind,source="$(DRIVERS_PATH)",target="/drivers" \
	$(APP):latest

docker-rmi:
	@-docker rmi -f $(docker images)

docker-rm:
	@-docker stop $(docker ps -a -q)
	@-docker rm $(docker ps -a -q)

start:  ##  start project in containers
	@-docker-compose up --build --remove-orphans -t 60 -d #--force-recreate

stop: docker-rm  #  stop project
	@-docker-compose stop
	@-docker-compose down