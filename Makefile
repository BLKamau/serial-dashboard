.PHONY: help run install test clean

# --- Default Command ---
.DEFAULT_GOAL:=help

# --- Command Targets ---

help:
	@printf "Available targets:\n"
	@printf "	run			Run project application\n"
	@printf "	install		Install project dependencies\n"
	@printf "	test		Run tests\n"
	@printf "	clean		Clean python cache\n"

run:
	poetry run python src/serial_dashboard/app.py

install:
	poetry install

test:
	poetry run pytest

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name __pycache__ -prune -exec rm -rf {} +

