install:
	poetry install
	
test:
	poetry run pytest hexlet_python_package tests
	

build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall
	

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build









brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

