install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black tests src

lint:
	flake8 src tests && \
		pylint tests/ src/

test:
	pytest tests

all: install format lint test