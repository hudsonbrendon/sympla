black:
	pipenv run black .

install:
	make black
	pipenv run python setup.py install

test:
	pipenv run python tests/tests.py

dev:
	make install
	make test