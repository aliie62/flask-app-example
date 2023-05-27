install:
	#install commands
	python -m pip install --upgrade pip &&\
    pip install -r requirements.txt
	#pip install -e .
lint:
	pylint --disable=R,C,W inventory/
test:
	coverage run -m pytest  -v -s
	coverage report -m --include=inventory/*
	coverage-badge -o coverage.svg -f
format:
	#format code
	black inventory/
all: install lint test format