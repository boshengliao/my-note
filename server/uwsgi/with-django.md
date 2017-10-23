使用 uwsgi + django 的配置文件  
=  

* uwsgi.ini  
  
        [uwsgi]
        socket = 127.0.0.1:port

        # manage.py 所在的目录
        chdir = /your/django/project/

        # 找到 wsgi.py 文件
        module = ysys.wsgi

        worker = 2
        threads = 2
        master = true

        # 指定 log 输出到目标位置
        daemonize = ysy.log

        # 在指定路径下生成 .pid 文件, 用于执行 uwsgi --reload app.pid 类似操作
        pidfile = ysy.pid

        # 请求头大小设置, 默认为 4k , 改为 32k
        buffer-size=32768
