install:
	#install commands
	python -m pip install --upgrade pip &&\
    pip install -r requirements.txt
	#pip install -e .
lint:
	pylint --disable=R,C,W inventory/
test:
	# pytest --cov=inventory
	coverage run -m pytest  -v -s
coverage_report:
	coverage report -m --include=inventory/*
	coverage-badge -o coverage.svg
format:
	#format code
	black inventory/
all: install lint test format