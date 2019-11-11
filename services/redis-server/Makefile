.PHONY: docs
SHELL := /bin/bash
PWD := $(shell pwd)
export REPOSITORY := sts-scraper-draper
export SERVICE_NAME := redis-server
export GITHUB_REGISTRY_HOST := $(shell source ../../config/.env && echo $$GITHUB_REGISTRY_HOST)
export GITHUB_USERNAME := $(shell source ../../config/.env && echo $$GITHUB_USERNAME)
export GITHUB_TOKEN := $(shell source ../../config/.env && echo $$GITHUB_TOKEN)
#  export VERSION := $(shell sed -ne '/current_version/s/current_version = //p' < setup.cfg)
export REGISTRY_PATH := $(GITHUB_REGISTRY_HOST)/$(GITHUB_USERNAME)/$(REPOSITORY)/$(SERVICE_NAME):$(VERSION)
export IMAGE_ID := $(shell docker images --filter=reference='$(SERVICE_NAME)' --format "table {{.ID}} {{.Repository}} {{.Tag}}" | head -2 | tail -1 | cut -d " " -f 1)
export GOOGLE_REGISTRY_PATH := us.gcr.io/$(REPOSITORY)

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

clean:
	@-rm -rf build dist *.egg-info htmlcov .coverage docs/build >> /dev/null
	@-find . -name '__pycache__' -exec rm -rf '{}' \; >> /dev/null

init:

bumpversion:  ## ustawia numer wersji
#	@-poetry run bumpversion minor --allow-dirty --list | grep new_version
	@-bumpversion --list minor | grep new_version | sed -r s,"^.*=",,
	@-git push origin master --tags

registry-logout:
	@-docker logout $(GITHUB_REGISTRY_HOST)

registry-login:
	@-docker login $(GITHUB_REGISTRY_HOST) -u $(GITHUB_USERNAME) -p $(GITHUB_TOKEN)

registry-build:  ## tworzy obraz dockera
	@-docker build -t $(SERVICE_NAME):latest --rm .

registry-upload:  ## wrzuca obraz dockera do rejestru GoogleCloud
	@-docker tag '$(IMAGE_ID)' $(GOOGLE_REGISTRY_PATH)/$(SERVICE_NAME):v$$(sed -ne '/current_version/s/current_version = //p' < setup.cfg)
	@-docker push $(GOOGLE_REGISTRY_PATH)/$(SERVICE_NAME):v$$(sed -ne '/current_version/s/current_version = //p' < setup.cfg)
#	@-docker rmi $(SERVICE_NAME):latest
