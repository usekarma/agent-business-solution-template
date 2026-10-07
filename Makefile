.PHONY: bootstrap test lint typecheck check

bootstrap:
	./scripts/bootstrap.sh

test:
	./scripts/test.sh

lint:
	.venv/bin/python -m ruff check .

typecheck:
	.venv/bin/python -m mypy src

check:
	./scripts/check.sh
