install:
	poetry install
	

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
