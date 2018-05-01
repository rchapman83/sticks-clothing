# -*- config:utf-8 -*-

import multiprocessing
import os


bind = '0.0.0.0:8080'
name = os.environ.get('PROJECT_NAME')
backlog = 2048
max_requests = 1000
proc_name = os.environ.get('PROJECT_NAME')
workers = int((multiprocessing.cpu_count() * 2) + 1)
threads = int(multiprocessing.cpu_count()+1)
daemon = False
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

forwarded_allow_ips = '*'