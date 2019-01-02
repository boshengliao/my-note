#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import json

from .base import BaseTest
from app.utility.log_cfg import log_unittest
from app.parser.models import ParserRecord


MODULE = '/parser'


class ParserRecordsCase(BaseTest):
    """
    """
    def setUp(self):
        self._set_up()
        self.prefix = self.app.application.config['APP_URL_PREFIX']
        return None

    def tearDown(self):
        if hasattr(self, 'tmp_oid'):
            self._delete(self.tmp_oid, ParserRecord)
        return None

    def test_post(self):
        """新建
        """
        url = '{}/{}/records'.format(
            self.prefix, MODULE
            )
        t = copy.deepcopy(self.test_parser_record)
        data = json.dumps(t)
        r = self.app.post(url, data=data)

        r = json.loads(r.data)
        assert r['error_code'] == 0
        assert r['data'] != ''

        self.tmp_oid = r['data']
        return None
