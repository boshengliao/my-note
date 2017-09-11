在 flask 中, 使用 celery 完成异步任务
=  

[参考文章](https://zhuanlan.zhihu.com/p/22304455)  

1. 在 flask 中, 使用 celery. `pip install celery`  
   * 新建文件, base.py:  
     
          from celery import Celery

          def make_celery(app):
              celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                              broker=app.config['CELERY_BROKER_URL'])
              celery.conf.update(app.config)
              TaskBase = celery.Task

              class ContextTask(TaskBase):
                  abstract = True

                  def __call__(self, *args, **kwargs):
                      with app.app_context():
                          return TaskBase.__call__(self, *args, **kwargs)
              celery.Task = ContextTask
              return celery  

   * 新建文件, beat_config.py:  

            from datetime import timedelta

            # 定义 celery beat (定时任务)
            CELERYBEAT_SCHEDULE = {
                'test-plan': {
                    'task': 'listen_buffer',
                    'schedule': timedelta(seconds=900),
                    # 'args': (110,),
                },
            }

            CELERY_TIMEZONE = 'UTC'

            # 尝试解决 celery worker 如下报错
            # ContentDisallowed: Refusing to deserialize untrusted content of
            # type pickle (application/x-python-serialize)
            CELERY_TASK_SERIALIZER = 'json'
            CELERY_RESULT_SERIALIZER = 'json'

   * 新建 `tasks.py` !!!这必须用单独的新文件, 很重要!!且 名字只能为 **tasks tasks tasks** !!  
     此时 base.py, beat\_config.py 和 \__init__.py, 放在新建的 /my\_celery/ 目录下, 且  
     tasks.py 在项目根目录, **必须**是**单独文件**, tasks.py:  
     
            import yaml

            from celery import platforms
            from celery.schedules import crontab

            from app_main import app
            from my_celery.base import make_celery
            from my_redis.my_redis import UseRedis
            from data_manager.save_data import CreateDatas
            from data_manager.pm_utils import MyUtils

            # 允许 root 用户允许 celery
            platforms.C_FORCE_ROOT = True

            # 配置 redis 地址
            app.config.update(
                CELERY_BROKER_URL='redis://localhost:6379/0',
                CELERY_RESULT_BACKEND='redis://localhost:6379/0'
            )

            # 生成 celery 实例
            # 命令行, 用 `celery worker -A tasks.celery --loglevel=info` 来启动
            # 在服务器用 supervisor 来保护 celery woker
            celery = make_celery(app)

            # 载入 celery config, 目前内含定时任务
            celery.config_from_object('my_celery.beat_config')

            # 定义一个 task 函数, 并将其命名为 listen_buffer
            @celery.task(name='listen_buffer')
            def listen_buffer():
                r = UseRedis()
                db = CreateDatas()
                u = MyUtils()
                try:
                    while 1:
                        # 从 redis 名为 'pm_datas' 的队列中, 获取值
                        t = r.get_value('pm_datas')

                        # 将 JSON 数据读取为 utf-8 编码
                        datas = yaml.safe_load(t)
                        # 过滤重复数据
                        tbname = 'PM_datas'
                        new_datas = u.get_valuable_datas(datas, tbname)

                        # 保存数据
                        if new_datas is not None:
                            db.create_datas(tbname, new_datas)
                        else:
                            print '没有可储存数据...'
                except TypeError as e:
                    print 'Current listen done, e: {}'.format(e)

     其中 **重要** 的点:
      1. 允许 root 用户允许 celery  
      2. 配置 redis 地址  
      3. 载入 celery config, 定时任务 beat 在 config 里面配置  
      4. 生成 celery 实例  
      5. 定义 celery 任务函数  

2. 在 flask 的 app.py 中, 也可以通过 `task_func_name.delay(params)` 手动执行 celery 任务:  

        from tasks import listen_buffer

        # 假设 listen_buffer 函数有参数, 则可以这样手动执行 celery 异步任务
        listen_buffer.delay(params)

3. 在 tasks.py 所在目录, 使用 `celery worker -A tasks.celery -l info` 来  
   启动 celery worker, 可以添加 `-c 10` 来开启10个 worker 进程.  

4. 在 tasks.py 所在目录, 使用 `celery beat -A tasks.celery -l info` 来  
   启动 celery beat, 用于**定时**派发**任务**给 worker 执行.

5. 在服务器端, 需要配合 [supervisor](http://blog.csdn.net/michael_lbs/article/details/75407089)
   来启动 **worker** .  
   我的 celery_worker.conf :  

            [program:pm_worker]
            # 用 django 则为项目目录. flask 则为虚拟环境中 celery 所在的 venv/bin 目录
            directory=/your/virtualenv/path/your-venv/bin/
            # 需要运行指令, 代替 `celery worker -A tasks.celery --loglevel=info` 开启 worker
            command=celery worker -A tasks.celery --loglevel=info
            autorestart=true
            loglevel=info
            redirect_stderr=true
            stdout_logfile=/var/log/supervisor/celery_worker.log
            environment=PYTHONPATH="$PYTHONPATH:/your/virtualenv/path/your-venv/lib/python2.7/site-packages"

   我的 celery_beat.conf :  

            [program:pm_beat]
            # 用 django 则为项目目录. flask 则为虚拟环境中 celery 所在的 venv/bin 目录
            directory=/your/virtualenv/path/your-venv/bin/
            # 需要运行指令, 代替 `celery beat -A tasks.celery --loglevel=info` 开启 beat
            command=celery beat -A tasks.celery --loglevel=info
            autorestart=true
            loglevel=info
            redirect_stderr=true
            stdout_logfile=/var/log/supervisor/celery_beat.log
            environment=PYTHONPATH="$PYTHONPATH:/your/virtualenv/path/your-venv/lib/python2.7/site-packages"

疑问:  
* 为什么 worker 在服务器端, 执行任务是**无规律间断式**的?  
  是否跟服务器**单核心**有关?  
  或者与**启动命令**有关? `celery worker -A tasks.celery -l info`