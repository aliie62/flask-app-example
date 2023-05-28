install:
	python -m pip install --upgrade pip &&\
    pip install -r requirements.txt
lint:
	pylint --disable=R,C,W inventory/
test:
	coverage run -m pytest  -v -s
	coverage report -m --include=inventory/*
	coverage-badge -o coverage.svg -f
format:
	black inventory/
build:
	docker buildx build -t inventory .
run:
	# create network
	# docker network create my_ntwork
	# docker run --network=my_ntwork --name redis-stack-server -d redis/redis-stack-server 
	# docker run -p 127.0.0.1:8080:8080 -e SQLITE_URI -e REDIS_HOST -e REDIS_PORT -e FLASK_SECRET_KEY --network=my_ntwork --name inventory inventory
all: install lint test format build