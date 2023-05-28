default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: install
install: # Install the project dependencies
	python -m pip install --upgrade pip &&\
    pip install -r requirements.txt

.PHONY: lint
lint: # Lint the code using pylint 
	pylint --disable=R,C,W inventory/

.PHONY: test
test: # Test the project and generates the coverage report and badge
	coverage run -m pytest  -v -s
	coverage report -m --include=inventory/*
	coverage-badge -o coverage.svg -f

.PHONY: format
format: # Format the code using Black
	black inventory/

.PHONY: build
build: # Create the Docker container of the project named "Inventory"
	docker buildx build -t inventory .

.PHONY: run
run: # Create Docker network, and run Inventory and Redis server containers
	docker network create my_ntwork
	docker run --network=my_ntwork --name redis-stack-server -d redis/redis-stack-server 
	docker run -p 127.0.0.1:8080:8080 -e SQLITE_URI -e REDIS_HOST -e REDIS_PORT -e FLASK_SECRET_KEY --network=my_ntwork --name inventory inventory
