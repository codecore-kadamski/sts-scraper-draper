SHELL := /bin/bash
PWD := $(shell pwd)
APP := sts.adamski.work
WORKON_HOME := env
APP_PATH := $(PWD)
ENV_PATH := $(APP_PATH)/$(WORKON_HOME)
#PID := $(shell cat app.pid)

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
        print("%-20s %s" % (target, help))
endef

export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

dbclear:  ## kasuje baze
	@-rm ./sts/migrations/0* 2>/dev/null || true
	@-python manage.py reset_db -c
	@-python manage.py migrate 2>/dev/null
	@-python manage.py makemigrations 2>/dev/null
	@-python manage.py migrate 2>/dev/null
	@-echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('kadamski', 'admin@myproject.com', '123')" | python manage.py shell

run:  ## local run
	@-python manage.py runserver

# start:  ## honcho start
# 	@-source ${ENV_PATH}/bin/activate && honcho start

# stop:  ##  honcho stop
# 	@-kill -9 $(PID)
# 	@-echo "" > app.pid

collectstatic:  ## Wgrywanie statykow
	@-source ${ENV_PATH}/bin/activate && python manage.py collectstatic --noinput 2>/dev/null || true

clearcache:  ## czysci cache
	@-find . -name "__pycache__" -exec rm -rf {} \; 2>/dev/null || true
	@-find . -name "*.pyc" -exec rm -rf {} \; 2>/dev/null || true
	@-find . -name ".pytest_cache" -exec rm -rf {} \; 2>/dev/null || true

migrations:  ## migracje
	python manage.py makemigrations 2>/dev/null
	python manage.py migrate 2>/dev/null
	python manage.py makemigrations 2>/dev/null

rm-migrations-mysql:  ## usuwa migracje mysql
	@-echo -e "${YELLOW}Usuwa migracje mysql i czysci baze jeśli jest${NC}"
	@-rm ./movie/migrations/0* 2>/dev/null || true
	@-echo -e "${RED}Potwierdzasz czyszczenie bazy <yes> <no> ?${NC}"
	@-python manage.py reset_db || true

develop:  ## tworzy lokalnie środowisko virtualne
	@-rm -rf ${WORKON_HOME}
	@-virtualenv --python=python3 ${WORKON_HOME}  #  virtualenv --python=python3 .venv
	@-source ${ENV_PATH}/bin/activate
	@-${ENV_PATH}/bin/pip install -r requirements.txt

dump_old:  ## zrzut starej bazy
	@-python manage.py sts --dump_old

restore_old:  ## import starej bazy
	@-python manage.py sts --restore_old

update_old:  ## update starej bazy: make update_old table=sport
	@-python manage.py sts --update_old=$(table)

sports:  ##  pobiera sporty
	@-python manage.py sts --sports

regions:  ##  pobiera regiony
	@-python manage.py sts --regions

leagues:  ##  pobiera ligi
	@-python manage.py sts --leagues

offerts:  ##  pobiera oferty
	@-python manage.py sts --offerts

update_results:  ##  aktualizacja wynikow
	@-python manage.py sts --update_results


volume:
	@-docker volume create --name pgdata


start: volume
	@-docker-compose up -d --force-recreate

stop:
	@-docker-compose stop
	@-docker stop stsdb
	@-docker rm stsdb
	#  @-rm -rf pgdata
