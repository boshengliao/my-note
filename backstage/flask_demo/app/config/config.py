# -*- coding: utf-8 -*-


class Config(object):
    """运维基础配置
    """
    # mongo
    MONGO_SETTINGS = [
        {
            'alias': 'default',
            'username': '',
            'password': '',
            'host': '',
            'port': 27017,
            'db': '',
        }
    ]

    # redis
    REDIS_PASSWORD = ''
    REDIS_HOSTNAME = ''
    REDIS_PORT = 6379
    REDIS_DB_INDEX = 0

    # sentry
    SENTRY_APP = ''
    SENTRY_CELERY = ''

    # oss
    OSS_ACCESSKEYID = ''
    OSS_ACCESSKEYSECRET = ''
    OSS_ENDPOINT = 'https://oss-cn-shanghai.aliyuncs.com'
    OSS_STS_ENDPOINT = 'https://sts.aliyuncs.com'
    OSS_BUCKET_URL = ''
    OSS_BUCKET_NAME = ''
    OSS_APIVERSION = '2015-04-01'
    OSS_DEFAULT_PROFILE_SECTION = 'Credentials'
    OSS_A = {
    }
