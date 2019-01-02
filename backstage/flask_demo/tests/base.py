# -*- coding: utf-8 -*-

import json
import sys
import os
import unittest

from bson import ObjectId

from app.app import app
from app.utility.log_cfg import log_unittest


class TestInstance(object):
    """测用例.
    引用id的字段在使用时再自行添加.
    """

    # 解析记录
    test_parser_record = {
    }


class BaseTest(unittest.TestCase, TestInstance):
    def _set_up(self):
        """配置flask测试环境
        """
        app.config['TESTING'] = True
        self.app = app.test_client()
        return None

    def _delete(self, _id, model=None):
        """删除测试数据
        """
        # 以下代码不要动
        model.objects.get(_id=_id).delete()
        return None

    def get_objectid(self):
        return str(ObjectId())

    # def _get_token(self):
    #     """通过登录拿到token
    #     """
    #     # 插入用户
    #     data = self.test_user
    #     loginname = data['loginname']
    #     password = data['password']

    #     user = User.objects(loginname=loginname).first()
    #     if user is None:
    #         user = User(**data)
    #         user.save()
    #     # 登录
    #     url = '{}/login'.format(PREFIX)
    #     t = {
    #         'loginname': loginname,
    #         'password': password,
    #     }
    #     data = json.dumps(t)

    #     r = self.app.post(url, data=data)
    #     r = json.loads(r.data)
    #     token = r['token']
    #     uid = user.reload()._id
    #     return uid, token

    # def get_headers(self):
    #     """获取构造headers
    #     """
    #     uid, token = self._get_token()
    #     headers = {
    #         'Authorization': 'Bearer {}'.format(token),
    #     }
    #     return headers, uid
