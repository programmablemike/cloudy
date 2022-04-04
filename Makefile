SHELL := /bin/bash

.PHONY: install
install:
	@python3 -m venv cloudy-env
	@source ./cloudy-env/bin/activate
	pip install -r requirements.txt

.PHONY: freeze
freeze:
	pip freeze > requirements.txt

.PHONY: run
run:
	@echo "Running the server"
	FLASK_APP=app.py flask run