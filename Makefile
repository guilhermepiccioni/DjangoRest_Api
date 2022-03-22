DOCKER_COMPOSE := docker-compose
FILE_NAME := products

# Execute containers, install requirements and release terminal.
.PHONY: build
build:
	$(DOCKER_COMPOSE) up -d --build

# Execute containers and running.
.PHONY: run
run:
	$(DOCKER_COMPOSE) up

# Stop all the containers and delete everything.
.PHONY: down
down:
	$(DOCKER_COMPOSE) down

# Create the migrations to models.
.PHONY: migrations
migrations:
	$(DOCKER_COMPOSE) exec server_django python manage.py makemigrations

# Populate the database with the model tables.
.PHONY: migrate
migrate:
	$(DOCKER_COMPOSE) exec server_django python manage.py migrate

# Create super user.
.PHONY: superuser
superuser:
	$(DOCKER_COMPOSE) exec server_django python manage.py createsuperuser


########## Starting the background ##########
.PHONY:start
start: build migrations migrate
	$(DOCKER_COMPOSE) up
