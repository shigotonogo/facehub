default: deps test

deps:
	pip install -r requirements.txt

test:
	nose2

.PHONY: deps test