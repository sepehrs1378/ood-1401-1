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

create-superuser:
	python manage.py ensure_it_manager --username=admin --password=admin --email=m.dehghankar@outlook.com

complete-run:
	make create-superuser && make migrate && make run
