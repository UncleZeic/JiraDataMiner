REVISION := $(shell git rev-parse HEAD)
VERSION := $(shell git rev-parse --abbrev-ref HEAD)

run:
	@echo "Running on ${VERSION} with revision ${REVISION}"
	@./main.py --hostname=${JIRA_HOSTNAME} --username=${JIRA_USERNAME} --password=${JIRA_PASSWORD}

help:
	@./main.py -h