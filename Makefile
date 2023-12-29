up:
	docker compose up -d
build:
	docker build . -t gemanueldev/recognition-django
buildUp:
	docker build . -t gemanueldev/recognition-django
	docker-compose up -d
buildUpLog:
	docker build . -t gemanueldev/recognition-django
	docker-compose up