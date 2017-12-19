使用 SQLALchemy 定义数据库模型, 使用 flask-migrate 做数据迁移  
=  

* 使用 sqlalchemy  
  [SQLALchemy官网](http://docs.sqlalchemy.org/en/rel_1_1/contents.html)  
  * 创建 models.py

        from datetime import datetime

        from sqlalchemy import (Column, ForeignKey, Integer, 
                                String, Boolean, DateTime, Float)
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.orm import relationship, sessionmaker
        from sqlalchemy import create_engine

        # 创建数据模型类
        Base = declarative_base()

        class User(Base):
            __tablename__ = 'user'

            # Column(字段名,　类型名)
            id = Column('id', Integer, primary_key=True)
            username = Column('账号', String(250))
            password = Column('密码', String(250))
            name = Column('名称', String(250))
            phone = Column('手机', String(250))
            email = Column('邮件', String(250))

            ＃ 浮点数的设置. asdecimal=True 显示小数位．
            ＃ decimal_return_scale=1 显示小数的位数．
            balance = Column('目标金额', Float(asdecimal=True, decimal_return_scale=1), default=0)


            # 建立外键
            group_id = Column('所属组id', Integer, ForeignKey('group.id'))

            # 建立外键的对象. backref='users' 为建立反向查询的属性
            group = relationship(Group, backref='users')

            # DateTime(True) 为是否设置时区
            create_date = Column('创建时间', DateTime(True), default=datetime.now())
            active = Column('可用状态', Boolean, default=True)

            def __repr__(self):
                return 'username: {}'.format(self.username)

  * 数据库初始化  

            """
                DBSession = sessionmaker(bind=engine)
                程序运行过程中, 有且仅建立运行一次. 重复运行会生成无用进程

                session = DBSession(), 生成 session 后, 用完必须关闭, session.close()
                否则会生成无用的进程
            """
            # 连接数据库的路径
            db_addr = ("postgresql+psycopg2://"
                       "qinziguan:qinziguan@localhost/qinziguan")
            engine = create_engine(db_addr)
            DBSession = sessionmaker(bind=engine)

            # 工具类
            class MyDb(object):
                def __init__(self):
                    self.DBSession = DBSession
                    self.Base = Base
                    return

                def set_up(self):
                    """
                        初始化数据库

                        self.Base.metadata.create_all(self.engine)
                        解释:
                            建立表, 对于已存在的表不会进行修改.
                            当使用 flask-migrate 时, 此条应注释, 通过 migrate, upgrade 建立表.
                            见下面 flask-migrate 介绍.
                    """
                    # self.Base.metadata.create_all(self.engine)

                    init_data = self.init_data
                    # 初始化 Group
                    datas = [dict(name='组1'), dict(name='组2')]
                    init_data(Group, datas)

                    return

                def get_session(self):
                    """
                        拿到 session 用于与数据库通信,
                        切记要提交 session.commit()
                        切记要关闭 session.close()
                    """
                    session = self.DBSession()
                    return session

                def init_data(self, model_name, datas):
                    """
                        初始化值, datas = [dict, dict, ...]
                    """
                    s = self.get_session()

                    model_name = model_name
                    datas = datas
                    for data in datas:
                        old = s.query(model_name).filter_by(**data).first()
                        t = old is None
                        if t:
                            new = model_name(**data)
                            s.add(new)

                    s.commit()
                    s.close()
                    return

* 使用 flask-migrate  
  [flask-migrate官网](http://flask-migrate.readthedocs.io/en/latest/)  

  * 创建 manage.py  

        from flask_script import Manager
        from flask_migrate import Migrate, MigrateCommand

        from your_package import app
        from database import models

        # 配置数据库地址
        app.config['SQLALCHEMY_DATABASE_URI'] = models.db_addr

        # 当数据库关闭时, 是否自动 commit
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

        # 获取数据库
        db = models.Base

        # 关联 app 和数据库
        migrate = Migrate(app, db)

        # 创建 db 命令, 例 python manage.py db init/migrate/upgrade/downgrade
        manager = Manager(app)
        manager.add_command('db', MigrateCommand)

        if __name__ == '__main__':
            # 这里很重要, 一定是 manager.run()
            manager.run()
