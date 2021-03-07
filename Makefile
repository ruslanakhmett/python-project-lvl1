install:
	poetry install

#test:
#	poetry run pytest hexlet_python_package tests

#lint:
#	poetry run flake8 hexlet_python_package

brain-games:
	poetry run brain-games

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
