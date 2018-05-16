flask添加url的根前缀  
=  

1. [参考资料](https://stackoverflow.com/questions/18967441/add-a-prefix-to-all-flask-routes)

2. example:

        from flask import Flask, url_for
        from werkzeug.serving import run_simple
        from werkzeug.wsgi import DispatcherMiddleware

        app = Flask(__name__)
        app.config['APPLICATION_ROOT'] = '/abc/123'

        @app.route('/')
        def index():
            return 'The URL for this page is {}'.format(url_for('index'))

        def simple(env, resp):
            resp(b'200 OK', [(b'Content-Type', b'text/plain')])
            return [b'Hello WSGI World']

        app.wsgi_app = DispatcherMiddleware(simple, {'/abc/123': app.wsgi_app})

        if __name__ == '__main__':
            app.run('localhost', 5000)