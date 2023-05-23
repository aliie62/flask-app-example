install:
	#install commands
	python -m pip install --upgrade pip &&\
    pip install -r requirements.txt
format:
	#format code
	black *.py models/*.py resources/*.py config/*.py
lint:
	pylint --disable=R,C *.py models/*.py resources/*.py config/*.py
all: install lint format