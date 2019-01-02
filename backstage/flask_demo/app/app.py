# -*- coding: utf-8 -*-

import datetime
import json
import logging
import os
import time

import jwt
from flask import request, jsonify, g, current_app
from bson.json_util import ObjectId

from . import request_context_utils as req_context
from app import create_app
from app.utility.log_cfg import log


app = create_app(os.environ.get('FLASK_ENV', None))


def parse_token(req):
    token = req.headers.get('Authorization').split()[1]
    return jwt.decode(token, app.config['SECRET_KEY'])


@app.before_request
def before_request():
    """请求前的处理
    """
    req_context.set_request_start_time()

    if req_context.is_white_url():
        return

    # 验证登录
    if not request.headers.get('Authorization'):
        return '您的请求未经授权', 401
    # noinspection PyBroadException
    try:
        payload = parse_token(request)
    except UnicodeDecodeError:
        return '授权口令错误', 401
    except Exception:
        return '授权口令过期，请重新登录', 401
    g.user_id = payload['sub']

    return


@app.after_request
def after_request(resp):
    if req_context.is_health_check():
        return resp

    new_resp = req_context.get_new_resp(resp)

    req_context.create_log(resp)
    return new_resp


@app.route('/', methods=['GET'])
def index():
    resp = 'hello world'
    return jsonify(resp)


@app.route('/check', methods=['GET'])
def check():
    resp = 200
    return jsonify(resp)
