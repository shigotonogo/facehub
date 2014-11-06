default: deps test

deps:
	pip install -r requirements.txt

test:
	nose2 -c nose2.cfg

run:
	python app/web/app.py

.PHONY: deps test