#!/usr/bin/env bash 
# выход при ошибке
 set -o errexit 

pip install -r require.txt 

python Manage.py Collectstatic --no-input 
Python Manage.py Migrate