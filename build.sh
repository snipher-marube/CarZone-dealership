#!/bin/bash

# Build the project
echo "Building the project..."
python3.12 -m pip install --upgrade pip

# Create a temporary requirements file for distutils and setuptools
echo "distutils" > temp-requirements.txt
echo "setuptools" >> temp-requirements.txt

# Install distutils and setuptools separately
pip3 install -r temp-requirements.txt

# Remove temporary requirements file
rm temp-requirements.txt

# Uninstall all packages
pip freeze | xargs pip uninstall -y

# Install required packages
pip install -r requirements.txt

echo "make migrations..."
python3.12 manage.py makemigrations
python3.12 manage.py migrate 

echo "collect static..."
python3.12 manage.py collectstatic --noinput --clear

echo "create default superuser..."
python3.12 manage.py create_default_superuser
