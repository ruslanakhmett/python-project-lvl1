install:
	poetry install

test:
	poetry run pytest brain_games tests

lint:
	poetry run flake8 brain_games


selfcheck:
	poetry check
	
check: selfcheck test lint
	

publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall


build:	check
	poetry build

.PHONY: install test lint selfcheck check build
