记录在 Flask 开发项目中遇到的一些问题  
=  

issues:  

1. 运行项目, `app.run(debug=true)`, 不能处理 POST 请求, 此时链接  
   处于 **pedding** 状态.  
   * 启动命令修改:  
     `app.run(debug=True, threaded=True)`  

2. nginx 中 location 指定 /test 时, 希望跳转到 flask 的 app.route("/").  
   * [解决文章](https://stackoverflow.com/questions/18967441/add-a-prefix-to-all-flask-routes)  
   * 内容待添加  

3. 在 flask 中, 使用 celery. `pip install celery`  
   * 新建文件, celery_func.py:  
     
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
    
   * 新建 task.py !!!这必须用, 很重要!!名字**必须**为 **task.py**:  
     
            import yaml

            from celery import platforms

            from app_main import app
            from celery_func import make_celery
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
            # 命令行, 用 `celery worker -A task.celery --loglevel=info` 来启动
            # 在服务器用 supervisor 来保护 celery woker
            celery = make_celery(app)

            #设置 celery 任务函数
            @celery.task
            def listen(data):
                # 将 JSON 数据读取为 utf-8 编码
                datas = yaml.safe_load(data)

                # 过滤重复数据
                tbname = 'PM_datas'
                u = MyUtils()
                new_datas = u.get_valuable_datas(datas, tbname)

                # 保存数据
                if new_datas is not None:
                    s = CreateDatas()
                    s.create_datas(tbname, new_datas)
                    message = '保存成功'
                    return message
                else:
                    message = '保存失败, 重复数据'
                    return message  

     其中 **重要** 的点:
      1. 允许 root 用户允许 celery  
      2. 配置 redis 地址  
      3. 生成 celery 实例  
      4. 设置 celery 任务函数  

4. 在 task.py 所在目录, 使用 `celery worker -A task.celery --loglevel=info` 来启动  
   celery worker, 可以添加 `-c 10` 来开启10个 worker 进程.  

5. 在服务器端, 需要配合 [supervisor](http://blog.csdn.net/michael_lbs/article/details/75407089)
   来启动 **worker** .  
   我的 celery_worker.conf :  

            [program:pm_worker]
            # 项目目录
            directory=/your/project/dir
            # 需要运行指令, 代替 `celery worker -A task.celery --loglevel=info` 开启 worker
            command=/your/virtualenv/path/your-venv/bin/celery worker -A task.celery --loglevel=info -c 4
            autorestart=true
            loglevel=info
            redirect_stderr=true
            stdout_logfile=/var/log/supervisor/celery.log
            environment=PYTHONPATH="$PYTHONPATH:/your/virtualenv/path/your-venv/lib/python2.7/site-packages"