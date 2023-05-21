#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

export REACT_APP_RENDER_GIT_COMMIT=$RENDER_GIT_COMMIT
yarn build

python manage.py collectstatic --no-input
python manage.py migrate
