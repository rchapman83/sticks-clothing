# -*- coding: utf-8 -*-
# Entry point to bring up the web app

from os import environ
import subprocess

c = environ.get('APP_CONFIG')
a = environ.get('APP_MODULE')

# Run Gunicorn to serve the app
try:
    print('START Green Unicorn')
    subprocess.call(['gunicorn', '-c', c, a])
except RuntimeError:
print('Unable to start application server')

# Run the Flask app server
# from app import sticksWeb
# sticksWeb.run(host='0.0.0.0', port=8080)
