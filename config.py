# -*- config:utf-8 -*-

import multiprocessing

bind = '0.0.0.0:8080'
name = 'sticks-clothing'
backlog = 2048
max_requests = 1000
proc_name = 'sticks-web'
workers = int((multiprocessing.cpu_count() * 2) + 1)
threads = int(multiprocessing.cpu_count()+1)
daemon = True
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

forwarded_allow_ips = '*'
# secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
