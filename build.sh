#!/bin/bash

# Build the project
echo "Building the project..."
python3.12 -m pip install --upgrade pip
pip3 install -r requirements.txt

echo "make migrations..."
python3.12 manage.py makemigrations
python3.12 manage.py migrate 

echo "collect static..."
python3.12 manage.py collectstatic --noinput --clear

echo "create default superuser..."
python3.12 manage.py create_default_superuser


