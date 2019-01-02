# -*- coding: utf-8 -*-

from mongoengine import connect
from pymongo import MongoClient

from app.config.config import Config


class DatabaseConfig(object):
    # 数据库配置
    def get_db(self, app):
        uri = self._get_uri(app)
        client = MongoClient(uri)

        db_name = app.config.get('MONGO_DATABASE')
        db = client[db_name]
        return db

    def init_app(self, app):
        """mongoengine connect setup.

        app.config须要有如下key:
            MONGO_SETTINGS = [
                {
                    'alias': 'default',
                    'username': 'test',
                    'password': 'test',
                    'host': '111.111.111.111',
                    'port': 27017,
                    'db': 'test',
                },
            ]
        """
        configs = self._get_configs(app)
        for config in configs:
            connect(**config)
        return None

    def _get_configs(self, app):
        # 配置
        settings = app.config['MONGO_SETTINGS']
        new_configs = []
        for config in settings:
            alias = config.get('alias', 'default')
            username = config.get('username', '')
            password = config.get('password', '')
            host = config.get('host', '')
            port = config.get('port', 27017)
            db = config.get('db', '')
            if not host or not db:
                msg = 'wrong mongo db config. host: {}, db: {}'.format(
                    host, db
                )
                raise ValueError(msg)
            # 构造 uri
            uri = 'mongodb://{}:{}/{}'.format(host, port, db)
            if username and password:
                uri = 'mongodb://{}:{}@{}:{}/{}'.format(
                    username, password, host, port, db
                )
            # 构造配置参数
            new = {
                'host': uri,
                'alias': alias,
            }
            new_configs.append(new)
        return new_configs
