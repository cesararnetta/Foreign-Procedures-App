#!/usr/bin/env bash
# exit on error
set -o errexit

npm install
npm run build

pipenv install

pipenv run upgrade

# python src/get_offices.py lo comento hasta que tengamos la API KEY en el environment, para ir haciendo pruebas de deploy

# python src/scraping.py no la ejecutamos localmente para obtener la información, después se podrá implementar con temporizador
# y servicos autimáticos a backend para alimentar la base de datos