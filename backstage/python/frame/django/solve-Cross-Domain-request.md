解决 django 和 angularJS 跨域请求(csrftoken, sessionid)
=

问题描述: 因为使用了前后端分离, 所以产生了跨域请求, csrftoken验证, 会话保持(sessionid)这  
三个问题.  

* 解决跨域: `pip install django-cors-headers`  

  1. 载入 app  

            INSTALLED_APPS = [
                '...',
                'corsheaders',  # 解决跨域请求的 app
            ]

  2. 添加中间件  

            MIDDLEWARE = [
                '...',
                # 必须在下面一条的前面, 顺序很重要!!
                'corsheaders.middleware.CorsMiddleware',
                'django.middleware.common.CommonMiddleware',
                '...',
            ]  

  3. 允许所有域通过  

            CORS_ORIGIN_ALLOW_ALL = True  

  4. 允许带 cookie 通过  

            CORS_ALLOW_CREDENTIALS = True  

     当前端发送 request 且含有 `withCredentials: true,` 时, 一定  
     要加上这条, 才能保证通信正常  

* 前端使用 js, jq, ng, ajx 等发送跨域 cookis, csrftoken, sessionid 验证时,  
  **http()** 里, 加入 `withCredentials: true,` 即可. 但是后端需要配合做  
  一些修改. 如:  

  1. 如 'Access-Control-Allow-Origin' 一定要是指定的域, 不能是 '*'.  
     'Access-Control-Allow-Credentials' 为 'True' 是允许带验证的请  
     求通过(cookie, csrftoken, sessionid)

            t = HttpResponse(r)
            t['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000, http://192.168.x.x:8000'
            t['Access-Control-Allow-Credentials'] = True
            t['Access-Control-Allow-Methods'] = 'GET, POST'
            t['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            return t

* 在 django 中取消表单验证 csrftoken,  
  'from django.views.decorators.csrf import csrf_exempt' 取消csrftoken验证.  
  然后在函数定义**前**加上装饰器 '@csrf_exempt', 即可解决表单验证.  

