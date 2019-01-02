# coding=utf-8
import os

from app.config.config import Config


class AppConfig(Config):
    """app基础配置
    """
    # 在生产环境时, 请确认DEBUG为false, 以确保配置正确
    DEBUG = True
    # 系统基础配置
    SECRET_KEY = ''

    # 白名单-填入url访问的endpoint, 用来取消对token的验证
    WHITE_ACCESS = {
    }

    APP_ROOT_PATH = os.path.split(os.path.abspath(__name__))[0]
    APP_URL_PREFIX = '/api'
    DATE_FORMAT = '%Y-%m-%d'
    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class ProductionConfig(AppConfig):
    DEBUG = False

    WHITE_ACCESS = {
        'check',
    }


class DevelopmentConfig(AppConfig):
    DEBUG = True

    WHITE_ACCESS = {
        '*',
    }


class TestingConfig(AppConfig):
    TESTING = True
