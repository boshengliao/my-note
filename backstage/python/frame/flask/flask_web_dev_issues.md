记录在 Flask 开发项目中遇到的一些问题  
=  

issues:  

1. 运行项目, `app.run(debug=true)`, 不能处理 POST 请求, 此时链接  
   处于 **pedding** 状态.  
   * 启动命令修改:  
     `app.run(debug=True, threaded=True)`  

2. nginx 中 location 指定 /test/ 时, 希望跳转到 flask 的 app.route("/").  
   * [解决文章](https://stackoverflow.com/questions/18967441/add-a-prefix-to-all-flask-routes)  

   * 核心内容:  

            from werkzeug.wsgi import DispatcherMiddleware

            app = Flask(__name__)
            app.config['APPLICATION_ROOT'] = '/test/'

            def simple(env, resp):
                resp(b'200 OK', [(b'Content-Type', b'text/plain')])
                return [b'Hello WSGI World']

            app.wsgi_app = DispatcherMiddleware(simple, {'/test/': app.wsgi_app})

