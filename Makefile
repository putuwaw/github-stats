env:
	cp .env.example .env

run:
	python app.py

py-install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

py-freeze:
	pip freeze > requirements.txt

tw-install:
	npm install -D tailwindcss
	npx tailwindcss init

tw-watch:
	npx tailwindcss -i ./static/styles/input.css -o ./static/styles/styles.css --watch

tw-minify:
	npx tailwindcss -o ./static/styles/styles.css --minify
