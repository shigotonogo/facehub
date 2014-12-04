default: deps test

deps:
	pip install tox

test:
	tox

.PHONY: deps test
