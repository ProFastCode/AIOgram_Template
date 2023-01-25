generate:
	alembic revision --autogenerate

migrate:
	alembic upgrade head

init:
	alembic init -t async bot/db/migrations
