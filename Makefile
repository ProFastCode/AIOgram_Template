# Refactoring
isort:
	poetry run isort bot/

black:
	poetry run black bot/

flake:
	poetry run flake8 bot/

lint: black isort flake


# Alembic
generate:
	alembic revision --autogenerate

migrate:
	alembic upgrade head

init:
	alembic init -t async bot/db/migrations