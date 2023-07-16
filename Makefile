env:
	cp .env.example .env

run:
	python app.py

py-install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

py-freeze:
	pip freeze > requirements.txt
