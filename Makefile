dev:
	python src/kokoro_be/main.py

start-dev-db:
	docker start kokoro-mysql

stop-dev-db:
	docker stop kokoro-mysql