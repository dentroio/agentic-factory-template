.PHONY: ci-local run test

test:
	python3 demo/test_greeting.py

ci-local: test

run:
	python3 demo/server.py
