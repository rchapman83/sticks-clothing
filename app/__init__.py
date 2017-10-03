# -*- coding: utf-8 -*-
# Flask web app

# Flask mod imports
from flask import Flask

# Construct application
sticksWeb = Flask(__name__.split('.')[0], static_folder='static', template_folder='templates')
sticksWeb.config.from_envvar('FLASK_SETTINGS')

# Import all the views for this web app
from . import routes
