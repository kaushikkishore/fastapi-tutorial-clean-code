# Makefile

.PHONY: test

test:
	python -m unittest discover -s tests -p 'test_*.py'
run: install
	uvicorn main:app --host 0.0.0.0 --port 8000

install:
	pip install -r requirements.txt