default: deps test

deps:
	pip install -r requirements.txt

test:
	nose2 -c nose2.cfg

.PHONY: deps test
