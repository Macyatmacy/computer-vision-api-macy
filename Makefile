install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C  celerec.py
	
test:
	python -m pytest -vv test_celerec.py


all: install lint test
