# -*- coding: utf-8 -*-

import datetime
import time
import json

from flask import request, g, jsonify, current_app

from .common.models import AccessLog


def set_request_start_time():
    request.start_time = time.time()
    return


def is_white_url():
    """检查白名单
    """
    white_list = current_app.config.get('WHITE_ACCESS', set())
    endpoint = request.endpoint

    if '*' in white_list:
        return True

    if endpoint not in white_list:
        return False

    return True


def is_health_check():
    """过滤健康检查接口
    """
    if request.path != '/check':
        return False
    return True


def get_new_resp(resp):
    """构造新的 response
    """
    data = resp.data.decode()
    try:
        data = json.loads(data)
    except json.JSONDecodeError:
        pass
    new_resp = {
        'error_code': 0,
        'msg': 'success',
        'data': '',
    }
    status_code = resp.status_code
    if not str(status_code).startswith('2'):
        new_resp.update(msg=data, error_code=status_code)
    else:
        new_resp.update(data=data)
    return jsonify(new_resp)


def create_log(resp):
    """为 request 创建 log.
    """
    status_code = resp.status_code
    error_code = status_code if not str(status_code).startswith('2') else 0

    access_log = AccessLog()
    access_log.args = {key: val for key, val in request.args.to_dict().items()}
    access_log.endpoint = request.endpoint
    access_log.create_time = datetime.datetime.now()
    access_log.creator_id = getattr(g, 'user_id', '')
    access_log.method = request.method
    access_log.seconds = time.time() - request.start_time
    access_log.error_code = error_code
    access_log.save()
    return
