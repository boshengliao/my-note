fabric 用于远程管理服务器  
=

非常灵活方便, 以下的介绍:  

* 参考[fabric指令介绍](http://blog.csdn.net/michael_lbs/article/details/70227720)
* 我的 fabfile.py:  
  
        #!/usr/bin/env python
        # -*- coding: utf-8 -*-

        from fabric.api import cd, env, prefix, run, task , sudo, hosts, execute, roles, local, lcd

        env.hosts = [
            'username@192.168.1.1: 22',
        ]

        env.passwords = {
            'username@192.168.1.1: 22': 'password',
        }

        @task(default=True)
        def remote():
            with cd('/home/my/work/projects-new/data-analysis-2'):
                with prefix('. vflask/bin/activate'):
                    with prefix('cd flask-accept-data/'):
                        run('git fetch origin master')
                        run('git merge --no-ff -m "merge with on-ff" origin/master')
                        with prefix('cd ../uwsgi_log/'):
                            run('uwsgi --reload app.pid')
                            sudo('service nginx restart')

        @task(default=True)
        def local():
            with lcd('/home/my/work/projects-new/data-analysis-2'):
                with prefix('. vflask/bin/activate'):
                    with prefix('cd uwsgi_log/'):
                        local('uwsgi --reload app.pid')
                        local('sudo service nginx restart')

        # 配置角色信息
        # env.user = 'username'
        # env.roledefs = {
        #     'role01': ['192.168.1.1'],
        #     'role02': ['192.168.1.2'],
        #     }
        # env.passwords = {
        #     'username@192.168.1.1: 22': 'yourpassword',
        #     'username@192.168.1.2: 22': 'yourpassword',
        # }

        # @roles('role01')
        # def test01():
        #     run('mkdir file01')

        # @roles('role02')
        # def test02():
        #     run('mkdir file02')

        # def allrun():
        #     execute(test01)
        #     execute(test02)
        #     execute(rxiio)