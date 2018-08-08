.PHONY: deploy
deploy: build
	twine upload dist/*

.PHONY: test-deploy
test-deploy: build
	twine upload --repository pypitest dist/*

.PHONY: build
build:
	python setup.py sdist bdist_wheel

.PHONY: test
test: install
	pytest

.PHONY: install
install:
	pip install . --upgrade


