migrate:
	python manage.py makemigrations && python manage.py migrate

run:
	python manage.py runserver 0.0.0.0:8000
	
run-docker:
	docker-compose up -d --build

start-db:
	docker-compose up -d --build app-db

stop:
	docker-compose stop

complete-run:
	make migrate && make run