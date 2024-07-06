#!/bin/bash

# Build the project
echo "Building the project..."
python3.9 -m pip install --upgrade pip
pip3 install distutils
pip3 install -r requirements.txt
pip3 install setuptools
pip3 freeze > requirements.txt

echo "make migrations..."
python3.9 manage.py makemigrations
python3.9 manage.py migrate 

echo "collect static..."
python3.9 manage.py collectstatic --noinput --clear

echo "create default superuser..."
python3.9 manage.py create_default_superuser
