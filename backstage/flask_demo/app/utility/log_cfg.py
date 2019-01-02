# -*- coding: utf-8 -*-

import logging
import os

# from flask import current_app
# from config.config import APP_ROOT_PATH


class Log(object):
    """配置logging
    """
    def __init__(self, proj_name='debug'):
        # 检查项目目录
        APP_ROOT_PATH = os.path.split(os.path.abspath(__name__))[0]
        folder = '{}/logs'.format(APP_ROOT_PATH)
        self._check_proj(folder)
        # 配置基础变量
        name = proj_name
        level = logging.INFO
        FORMAT = ('%(asctime)s-%(name)s-%(levelname)s: %(message)s')
        file_name = '{}/{}.log'.format(folder, proj_name)

        # 生产logger实例
        logger = logging.getLogger(name)

        # 判断logger是否存在
        t = logger.handlers
        if len(t) != 0:
            self.logger = logger
            return None

        # 构造格式
        formatter = logging.Formatter(FORMAT)
        logger.setLevel(level=level)

        # 构造file
        handler = logging.FileHandler(file_name)
        handler.setLevel(level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # 构造stream
        # console = logging.StreamHandler()
        # console.setLevel(level)
        # console.setFormatter(formatter)
        # logger.addHandler(console)

        self.logger = logger
        return None

    def log(self, message, exc_info=True):
        """输出信息
        """
        self.logger.info(message, exc_info=exc_info)
        # return None

    def _check_proj(self, proj_name):
        """检查项目文件夹是否存在. 不存在, 则创建
        """
        t = os.path.exists(proj_name)
        if not t:
            os.mkdir(proj_name)
        return None


# 函数
log = Log().log
log_unittest = Log('unittest').log
