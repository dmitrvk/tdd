test:
	pytest fibonacci money
	python -m xunit.tests
	flake8 fibonacci money xunit
