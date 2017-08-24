用 django 里的 class 快速建立 dict  
=  

在开发过程中经常会出现需要把 django 的 class 构造成 对象/dict 的形式, 以方便 json 序列化.  
例如:  

1. 已经存在的 model :

        class User(models.model):
            name = models...
            age = models...
            addr = models...
    
2. 需要构建的对象:  

        # 一般的操作
        u = User.objects.get(id=1)
        r = {
            'id', u.id,
            'name', u.name,
            'age', u.age,
            'addr', u.addr,
        }

3. 偷懒的 api:  

        def get_objs_ditc(self, data):
            # data 为一个对象列表 [obj1, obj2, ...]
            # 获取 obj dict, 并删除以 '_'起头的内部 key
            objs = []
            for i in data:
                # 用 obj.__dict__ 帮助直接获得 dict 化的结果
                r = i.__dict__
                # 从 dict 里面删除我们不需要的内部 key, 通常以 '_' 起头
                for ii in r.keys():
                    if ii[0] == '_':
                        r.pop(ii)
                objs.append(r)

            return objs