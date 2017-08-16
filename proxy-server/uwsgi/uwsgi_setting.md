记录 uwsgi+nginx+flask 基础配置
=

1. [uwsgi官网](http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html)
   内含 quick start, 配置文件.  

2. my_uwsgi.ini:  

        [uwsgi]
        socket = ip:port

        # 还可以选择用 .socket 文件启动
        # socket = /your/path/app.socket

        # app 启动前切换至项目路径, 否则载入 mould 会报错
        chdir = /your/project/

        # 项目文件
        wsgi-file = app_main.py

        worker = 2
        threads = 2
        master = true

        # 启动 flask 项目中的 app
        callable = app

        # 指定 log 输出到目标位置
        daemonize = /your/app.log

        # 请求头大小设置, 默认为 4k , 改为 32k
        buffer-size=32768

        # true 时, 不记录请求信息的日志。只记录错误以及uWSGI内部消息到日志中。
        #disable-logging = true

        #log-maxsize = 1024

        # 启动时, 切分日志
        #log-truncate = true

        #processes = 4
        #threads = 2
        #stats = 127.0.0.1:9191

        #virtualenv = /your/virtualenv

3. 在项目所在路径下, 执行:  
   `uwsgi -s /your/path/app.socket -w app_main:app`  
   即可在 `/your/path/` 路径下, 获得 **.socket** 文件  

4. 配置 nginx 中的 uwsgi:  

        location / {
            uwsgi_pass ip:port;
            # 这里还有一种配置. 选择何种方式都需要与 app_uwsgi.ini 文件一样
            # uwsgi_pass unix:/your/path/app.socket;

            include uwsgi_params;

            proxy_http_version 1.1;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        }

   * 这里有一个疑问, 当更改 location 的 `/` 为 `/test/` 时, 如何在 flask  
     让 `/test/` 访问 `app.route("/")`.  
     当前情况是浏览器 输入 `/test/`,则会直接去 flask 里寻找对应的 `app.route("/test/")`.  
     如果没找到, 则 404.  

5. 启动 `uwsgi`, 在 `your/path/app_uwsgi.ini` 目录执行:  
   `uwsgi app_uwsgi.ini`  
   此时可以去查看 **.log** 文件是否有报错信息.