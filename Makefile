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

.PHONY: test
test:
	python -m unittest discover tests/ "*_test.py"

.PHONY: docker-build
docker-build:
	docker build -f Dockerfile -t cloudy:latest .

.PHONY: docker-run
docker-run:
	docker run -it --rm --publish-all cloudy:latest