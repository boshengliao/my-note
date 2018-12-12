celery的监控工具  
=

[flower](https://github.com/mher/flower)  

* 启动`celery -A app.tasks flower --conf=app/flowerconfig.py`  
  * 配置文件--flowerconfig.py:

            # -*- coding: utf-8 -*-

            db = 'flower_db'
            port = 8083
            address = '0.0.0.0'
            persistent = True
            basic_auth = ['username:password']
