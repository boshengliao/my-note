# -*- coding: utf-8 -*-

import json

from flask import make_response

from . import errors


def register_error_handlers(app):
    """注册错误处理函数
    """
    config = [
        (errors.ValidationError, ErrorHandler.mongo_error),
        (errors.NotUniqueError, ErrorHandler.mongo_unique),
        (errors.Schema_ValidationError, ErrorHandler.schema_error),
        (errors.GeneralError, ErrorHandler.general_error),
    ]

    register = app.register_error_handler
    for error, handler in config:
        register(error, handler)
    return


class ErrorHandler(object):
    """错误处理函数工具
    """
    @staticmethod
    def mongo_error(e):
        """mongoengine error handler func.
        """
        msg = json.dumps(e.message)
        error_code = 4602
        resp = make_response(msg)
        resp.status_code = error_code
        return resp

    @staticmethod
    def mongo_unique(e):
        """处理字段unique的情况
        """
        msg = json.dumps(e.args)
        error_code = 4602
        resp = make_response(msg)
        resp.status_code = error_code
        return resp

    @staticmethod
    def general_error(e):
        """处理一般的情况
        """
        msg = json.dumps(e.args)
        error_code = 4600
        resp = make_response(msg)
        resp.status_code = error_code
        return resp

    @staticmethod
    def schema_error(e):
        """处理marshmallow的情况
        """
        msg = json.dumps(e.messages)
        error_code = 4601
        resp = make_response(msg)
        resp.status_code = error_code
        return resp
