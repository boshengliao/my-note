# -*- coding: utf-8 -*-

"""对`model`进行公共操作的工具
"""

import datetime

from bson import ObjectId
from flask import current_app as app
from mongoengine import Document, queryset_manager, QuerySet
from mongoengine import StringField, BooleanField, IntField, DateTimeField
from mongoengine import ListField, DictField, FloatField

from app import errors
from app.utility.log_cfg import log
from app.utility.paginate import Page


class BaseDocument(Document):
    """基础字段
    """
    create_time = DateTimeField(verbose_name="创建时间")
    update_time = DateTimeField(verbose_name="更新时间")
    is_active = BooleanField(verbose_name="状态", default=True)

    meta = {
        'abstract': True,
        'queryset_class': Page,
    }

    def clean(self):
        if not getattr(self, '_id', ''):
            self._id = str(ObjectId())
        return None

    @queryset_manager
    def find(doc_cls, queryset):
        """替代`model.objects()`, 默认筛选`is_active=True`的数据.
        """
        return queryset.filter(is_active=True)


class AssistMethod(object):
    """`model`辅助方法类
    """
    @classmethod
    def new_create(cls, data):
        """创建一个对象
        """
        now = cls.get_now()
        data.update(create_time=now, update_time=now)
        obj = cls(**data).save()
        return obj

    def new_update(self, data):
        """更新一个对象
        """
        now = self.get_now()
        data.update(update_time=now)
        self.update(**data)
        self.reload()
        return self

    def new_destroy(self):
        """销毁一个对象
        """
        now = self.get_now()
        self.update(update_time=now, is_active=False)
        return None

    @staticmethod
    def get_now(datetime_fmt=None):
        """获取当前时间的字段串
        """
        if datetime_fmt is None:
            try:
                datetime_fmt = app.config['DATETIME_FORMAT']
            except Exception:
                raise errors.GeneralError(
                    'get DATETIME_FORMAT error from app.'
                )

        now = datetime.datetime.now().strftime(datetime_fmt)
        return now
