.ONESHELL:
.PHONY: clean run env pip help

REVISION := $(shell git rev-parse HEAD)
VERSION := $(shell git rev-parse --abbrev-ref HEAD)

run:
	@echo "Running on ${VERSION} with revision ${REVISION}"
	@./main.py --hostname=${JIRA_HOSTNAME} --username=${JIRA_USERNAME} --password=${JIRA_PASSWORD}

env:
	@python3 -m venv dev
	
pip:
	@pip install --upgrade pip
	@pip install -r ./requirements.txt

clean:
	@rm -rf dev
	@find . -name "*.pyc" -delete

help:
	@./main.py -h
