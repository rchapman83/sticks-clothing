# -*- coding: utf-8 -*-
# All the views here

# Import app via circular imports
from . import sticksWeb
# Import flask stuff
from flask import Flask, render_template, request, url_for, send_from_directory

@sticksWeb.route('/')
def entry():
        return render_template('index.html')

@sticksWeb.route('/backend')
def back():
        return 'logon page'

@sticksWeb.route('/robots.txt')
def robots_static():
  return send_from_directory(application.static_folder, request.path[1:])

@sticksWeb.route('/sitemap.xml')
def sitemap_static():
  return send_from_directory(application.static_folder, request.path[1:])

@sticksWeb.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@sticksWeb.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500
