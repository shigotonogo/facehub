PYTHON3=python
default: deps test

deps:
	pip install -r requirements.txt

test:
	tox

run: deps
	$(PYTHON3) -V
	$(PYTHON3) services/app.py

.PHONY: deps test
