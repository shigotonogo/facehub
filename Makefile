default: deps test

deps:
	pip install -r requirements.txt

test:
	nose2 -c nose2.cfg

run:
	python facehub/app.py

.PHONY: deps test
