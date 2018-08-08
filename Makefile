deploy: build
	twine upload dist/*

test-deploy: build
	twine upload --repository pypitest dist/*

build:
	python setup.py sdist bdist_wheel

test: install
	pytest

install:
	pip install . --upgrade


