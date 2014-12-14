PYTHON3=python
default: deps test

deps:
	pip install tox
	pip install -r test-requirements.txt

test: deps
	tox

run: deps
	$(PYTHON3) -V
	$(PYTHON3) services/app.py

.PHONY: deps test
