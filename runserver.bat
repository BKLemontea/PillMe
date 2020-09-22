@echo off

python manage.py runsslserver 0.0.0.0:8080 --certificate cert/django.cert --key cert/django.key