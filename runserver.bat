@echo off

python manage.py runsslserver 0.0.0.0:8000 --certificate cert/django.cert --key cert/private.key