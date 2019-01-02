# -*- coding: utf-8 -*-

import multiprocessing
import os

# from config.config import APP_ROOT_PATH, DEBUG

APP_ROOT_PATH = '/app'
DEBUG = False

LOG_FOLDER = '{}/logs'.format(APP_ROOT_PATH)
try:
    os.mkdir(LOG_FOLDER)
except Exception:
    pass

bind = '0.0.0.0:9010'
workers = 2 if DEBUG else multiprocessing.cpu_count()
worker_class = "gevent"  # sync, gevent,meinheld
worker_connections = 2 if DEBUG else 10
accesslog = '{}/access.log'.format(LOG_FOLDER)
errorlog = '{}/error.log'.format(LOG_FOLDER)
max_requests = 100
pidfile = '{}/gunicorn.pid'.format(LOG_FOLDER)
