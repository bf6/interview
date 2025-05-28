.PHONY: help up test makemigrations migrate down logs shell

help: ## Show this help message
	@echo 'Usage:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

up: ## Start the application with Docker Compose and watch for changes
	docker-compose up --watch

rebuild: ## Rebuild the application with Docker Compose
	docker-compose up --build --watch

test: ## Run Django tests
	docker-compose exec -it backend ./manage.py test

makemigrations: ## Create new database migrations
	docker-compose exec -it backend ./manage.py makemigrations

migrate: ## Apply database migrations
	docker-compose exec -it backend ./manage.py migrate

down: ## Stop and remove Docker containers
	docker-compose down

logs: ## View Docker container logs in real-time
	docker-compose logs -f

shell: ## Open Django shell
	docker-compose exec -it backend ./manage.py shell

backend_container: ## Open a shell in the backend container
	docker-compose exec -it backend /bin/bash

frontend_container: ## Open a shell in the frontend container
	docker-compose exec -it frontend /bin/bash







.DEFAULT_GOAL := help
