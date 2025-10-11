.PHONY: deps test clean
BIN=.venv/bin/
PYTHON=python3

deps:
	$(PYTHON) -m venv .venv
	$(BIN)pip install --upgrade pip
	$(BIN)pip install -r requirements.txt
	$(BIN)pip install -e .

test:
	$(BIN)python -m unittest discover tests/

clean:
	rm -rf .venv
	find . -iname "*.pyc" -delete
	find . -iname "__pycache__" -delete
