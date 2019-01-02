# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from .error_handlers import register_error_handlers
from app.utility.prefix_config import PrefixConfig
from app.utility.mongo_cfg import DatabaseConfig
from app.utility.log_cfg import log


def create_app(flask_env=None):
    # init
    app = Flask(__name__)

    # 读取配置
    config_app = {
        'development': 'app.app_config.DevelopmentConfig',
        'production': 'app.app_config.ProductionConfig',
    }
    if flask_env:
        app.config.from_object(config_app.get(flask_env))

    # 设置跨域
    CORS(app)

    # 设置api前缀
    PrefixConfig().init_app(app)

    # connect mongo
    DatabaseConfig().init_app(app)

    # 注册蓝图
    config_blueprints = [
        # ('app.module_name.blueprint', 'blueprint', ''),
    ]
    register_blueprints(app, config_blueprints)

    # 注册错误处理
    register_error_handlers(app)
    return app


def register_blueprints(app, config):
    """注册蓝图
    """
    for model_path, blueprint_name, url in config:
        model = __import__(model_path, fromlist=1)
        blueprint = getattr(model, blueprint_name, '')
        if not blueprint:
            continue
        url_prefix = blueprint.url_prefix
        if not url:
            url = url_prefix
        app.register_blueprint(blueprint, url_prefix=url)
    return


def add_resource(app, config):
    """添加restful资源配置
    """
    api = Api(app)
    for view, url in config:
        api.add_resource(view, url)
    return
