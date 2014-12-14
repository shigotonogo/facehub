PYTHON3=python
default: deps test

deps:
	pip install tox
	pip install -r test-requirements.txt

test: deps
	tox

fixtures:
	./fixtures

run: deps fixtures
	$(PYTHON3) facehub/app.py

.PHONY: deps test
