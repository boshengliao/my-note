# -*- coding: utf-8 -*-

from mongoengine import QuerySet


class Page(QuerySet):
    """跟分页有关的 api
    """
    def get_page_data_and_info(self, **params):
        """将数据分页且给出分页信息.
        params: {
            order_by: str, 排序的字段, -_id/_id[ name age phone ...].
            per_page: str, 每页显示数量.
            current_page: str, 当前页码.
        }
        """
        self._set_paginate_params(params)

        page_queryset = self._get_page_queryset()
        page_info = self._get_page_info()
        return page_queryset, page_info

    def _get_page_queryset(self):
        """获取分页后的`queryset`
        """
        r = (self.order_by(*self.order_by_values)
                 .skip(self.skip_num).limit(self.limit_num))
        return r

    def _get_page_info(self):
        """获取分页信息
        """
        page_info = {
            'total_num': self.total_num,
            'total_page': self.page_num,
            'current_page': self.current_page,
            'prev_page': self.prev_page,
            'next_page': self.next_page,
        }
        return page_info

    def _set_paginate_params(self, params):
        """设置分页参数
        """
        self._params = params
        return

    @property
    def total_num(self):
        if not hasattr(self, '_total_num'):
            self._total_num = self.count()
        return self._total_num

    @property
    def current_page(self):
        default = 1
        args = getattr(self, '_params', {})
        _current_page = args.get('current_page', default)

        try:
            _current_page = int(_current_page)
        except ValueError:
            _current_page = default

        if _current_page <= 0:
            _current_page = default
        return _current_page

    @property
    def per_page(self):
        default = 10
        args = getattr(self, '_params', {})
        _per_page = args.get('per_page', default)

        try:
            _per_page = int(_per_page)
        except ValueError:
            _per_page = default

        if _per_page <= 0:
            _per_page = default
        return _per_page

    @property
    def prev_page(self):
        _prev_page = self.current_page - 1

        if _prev_page < 1:
            _prev_page = 1
        return _prev_page

    @property
    def next_page(self):
        _next_page = self.current_page + 1

        if _next_page > self.page_num:
            _next_page = self.page_num
        return _next_page

    @property
    def page_num(self):
        _page_num = self.total_num // self.per_page
        if self.total_num % self.per_page != 0:
            _page_num += 1
        return _page_num

    @property
    def order_by_values(self):
        """排序值
        args: dict, 内含order_by.
        """
        # sort 条件
        default = '-_id'
        args = getattr(self, '_params', {})
        values = args.get('order_by', default).split()
        return values

    @property
    def skip_num(self):
        """跳过值
        """
        default = 0
        skip_num = (self.current_page-1) * self.per_page
        if skip_num < 0:
            skip_num = default
        return skip_num

    @property
    def limit_num(self):
        """limit值
        """
        return self.per_page
