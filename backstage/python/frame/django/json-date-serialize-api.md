django 中, 用 json 序列化 datetime 以及 date
=  

直接使用 `json.dumps(obj)` 会报错, 提示 **datetime/date** type not json serialize 类似  
的错误, 那么现在:  

1. 构造一个检查函数:  

        def _json_date_serialize(self, obj):
            if isinstance(obj, datetime):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(obj, date):
                return obj.strftime('%Y-%m-%d')
            else:
                raise TypeError('%r is not JSON serializable' % obj)

2. 使用 `json.dumps(obj, default=self.\_json\_date_serialize)` 即可按上面格式  
   来 json 序列化 **datetime/date** 类型.