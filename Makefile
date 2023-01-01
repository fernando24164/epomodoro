test:
	python -m unittest discover -p 'test_*' -s 'tests'
	rm -r *.pickle
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +