#!/bin/sh
# entry point for api

set -a 
source /home/Triest/.env
set +a

set -e

# migrate runs

cd /home/Triest/info

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py runserver 
