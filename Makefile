install:
	#install commands
	python -m pip install --upgrade pip &&\
    pip install -r requirements.txt
	#pip install -e .
lint:
	pylint --disable=R,C,W inventory/
test:
	pytest -vv --cov=inventory
format:
	#format code
	black inventory/
all: install lint test format