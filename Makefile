PYTHON3=python
default: deps test

deps:
	pip install tox
	pip install -r requirements.txt
	pip install -r test-requirements.txt

test: deps
	tox

# dbseeds:
# 	./dbseeds

run: deps dbseeds
	$(PYTHON3) facehub/app.py

.PHONY: deps test dbseeds
