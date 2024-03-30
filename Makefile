# инструкция по работе с файлом "Makefile" – https://bytes.usc.edu/cs104/wiki/makefile/

# обновление сборки Docker-контейнера
build:
	MSYS_NO_PATHCONV=1 docker compose build

# генерация документации
docs-html:
	MSYS_NO_PATHCONV=1 docker compose run --workdir /docs app /bin/bash -c "make html"

# запуск форматирования кода
format:
	MSYS_NO_PATHCONV=1 docker compose run --workdir / app /bin/bash -c "black src docs/source/*.py; isort --profile black src/*.py docs/source/*.py"

# запуск статического анализа кода (выявление ошибок типов и форматирования кода)
lint:
	MSYS_NO_PATHCONV=1 docker compose run --workdir / app /bin/bash -c "pylint --load-plugins pylint_django --load-plugins pylint_django.checkers.migrations --django-settings-module=portfolio.settings src; flake8 src; mypy src; black --check src"

# запуск автоматических тестов
test:
	MSYS_NO_PATHCONV=1 docker compose run app ./manage.py test

# запуск всех функций поддержки качества кода
all: format lint test
