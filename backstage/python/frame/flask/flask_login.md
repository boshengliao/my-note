关于 flask-login 的实例  
=  

[flask-login官方文档](https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager)  

* [参考文章: Flask-Login 使用和进阶](http://www.ttlsa.com/python/flask-login-using-and-advanced/)  

* 创建 login_config.py:  
  
        #!/urs/bin/env python3
        # -*- coding: utf-8 -*-

        from flask_login import LoginManager

        # from yourfile import app
        from database.models import UserModel, MyDb


        login_manager = LoginManager()

        # 必须要有 secret_key
        # app.secret_key = '!@# your key $%^'

        # 可以在 app 文件里载入 login_manager, 从而初始化
        # login_manager.init_app(app)

        # 在没有登录的情况下, 返回 login_view 定义的视图或者 url
        login_manager.login_view = "/"
        # session 保护程度
        login_manager.session_protection = "strong"
        login_manager.login_message = "Please login to access this page."
        login_manager.login_message_category = "info"


        @login_manager.user_loader
        def load_user(user_id):
            """
                为 flask-login 重载时,
                返回登录的对象, 否则返回 None
            """
            db = MyDb()
            s = db.get_session()

            user = s.query(UserModel).get(user_id)

            s.close()
            return user

* app.py 内容:  

        from flask import Flask, redirect, url_for, request
        from flask_restful import Resource, Api
        from flask_login import login_user, logout_user, login_required
        from login_config import login_manager
        from views.login import Login
        from views.logout import Logout

        app = Flask(__name__)
        app.secret_key = '!@% your key #$'
        api = Api(app)

        # flask-login
        login_manager.init_app(app)


        class HelloWorld(Resource):
            @login_required
            def get(self):
                return {'hello': 'world'}


        # views
        api.add_resource(HelloWorld, '/hi')
        api.add_resource(Login, '/login')
        api.add_resource(Logout, '/logout')

        @app.route("/")
        @login_required
        def hello():
            t = 'hello world'
            return t

* login.py:  

        class Login(Resource):
            def __init__(self):
                self.db = MyDb()

                self.UserModel = UserModel

                self.HandleObj = HandleObj

                self.login_user = login_user
                return

            @login_required
            def get(self):
                r = 'welcome to login page...'
                return r

            def post(self):
                data = request.form

                k = 'username'
                username = data[k]
                k = 'password'
                password = data[k]

                s = self.db.get_session()
                m = self.UserModel
                user = s.query(m).filter_by(username=username).first()

                # 验证密码
                pw = user.password
                t = pw == password
                if t:
                    self.login_user(user)
                    h = self.HandleObj()
                    r = h.get_objs_dict(user)
                else:
                    r = None

                s.close()
                return r

* logout.py:  

        class Logout(Resource):
            def __init__(self):
                self.logout_user = logout_user
                return

            def get(self):
                r = 'welcome to logout page...'
                return r

            def post(self):
                self.logout_user()
                return None

* 关于 **@login_required** 的两种用法:  
  1. 是直接在视图函数上使用, 如:  

            @app.route("/")
            @login_required
            def hello():
                t = 'hello world'
                return t

  2. 是在 restful 视图类的方法商用, 如:  

            class Login(Resource):

                @login_required
                def get(self):
                    r = 'welcome to login page...'
                    return r
