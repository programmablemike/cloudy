SHELL := /bin/bash
DOCKER_IMAGE := cloudy
DOCKER_IMAGE_TAG := latest

VENV := ./cloudy-env
VENV_ACTIVATE = ./$(VENV)/bin/activate
TESTS_DIR := tests/
TESTS_PATTERN := "*_test.py"

.PHONY: install
install:
	@python3 -m venv $(VENV)
	. $(VENV_ACTIVATE) && pip install -r requirements.txt

.PHONY: freeze
freeze:
	. $(VENV_ACTIVATE) && pip freeze > requirements.txt

.PHONY: run
run:
	@echo "Running the server"
	. $(VENV_ACTIVATE) && FLASK_APP=app.py flask run

.PHONY: test
test:
	. $(VENV_ACTIVATE) && python -m unittest discover $(TESTS_DIR) $(TESTS_PATTERN)

.PHONY: docker-build
docker-build:
	docker build -f Dockerfile -t $(DOCKER_IMAGE):$(DOCKER_IMAGE_TAG) .

.PHONY: docker-run
docker-run:
	docker run -it --rm --publish-all $(DOCKER_IMAGE):$(DOCKER_IMAGE_TAG)