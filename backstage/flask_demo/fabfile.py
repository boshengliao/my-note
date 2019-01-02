#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from fabric.api import (cd, env, prefix, run, task, sudo,
                        hosts, execute, roles, local, lcd)

# 服务器配置
# USER = ''
USER = 'root'
USER_PW = ''
IP_API = ''
# USER_API = 'root'
# USER_PW_API = ''
# IP_CELERY = ''
# USER_CELERY = ''
# USER_PW_CELERY = ''
# env.hosts = [
#     USER_ROOT,
# ]
# env.passwords = {
#     USER_ROOT: USER_ROOT_PW,
# }
env.user = USER
env.roledefs = {
    'api': [IP_API],
    # 'celery': [IP_CELERY],
}
env.passwords = {
    '{}@{}'.format(USER, IP_API): USER_PW,
    # '{}@{}'.format(USER, IP_CELERY): USER_PW,
}

# 项目路径
PROJ_NAME = ''
LOCAL_PATH = os.path.abspath('')
REMOTE_PATH = ''

# git配置
ORIGIN = 'origin'
DEV = 'develop'

# 容器仓库用户配置
USER = ''
PW = ''

# 容器配置
PUBLIC = 'registry.cn-shanghai.aliyuncs.com'
PVC = 'registry-vpc.cn-shanghai.aliyuncs.com'
NAMESPACE = ''
IMAGENAME = PROJ_NAME
IMAGE_VERSION = 'latest'
CONTAINER_DEV = '{}_api'.format(PROJ_NAME)
CONTAINER_DEV_CELERY = '{}_celery'.format(PROJ_NAME)
COMPOSE_NAME_CELERY = 'celery'


@roles('api')
@task(default=True)
def dev(directive, *args, **kw):
    """开发环境用
    """
    u = Utils()
    cfg = {
        'p': u.push_fetch_merge,
        'l': u.docker_log,
        'r': u.docker_restart,
        'b': u.docker_bash,
        'dp': u.docker_update_image,
    }

    if directive not in cfg:
        print('没有该指令')
        return None
    f = cfg[directive]
    f(CONTAINER_DEV)
    return None


class Utils(object):
    """fabric工具
    """
    def push_fetch_merge(self, *args, **kw):
        """推送本地develop分支到远程库, 再在服务器下拉代码
        """
        with lcd(LOCAL_PATH):
            t = 'git checkout {}'.format(DEV)
            local(t)
            t = 'git push {} {}:{}'.format(ORIGIN, DEV, DEV)
            local(t)

        self.remote_fetch_merge()
        return None

    def remote_fetch_merge(self, *args, **kw):
        """远程服务器合并代码
        """
        with cd(REMOTE_PATH):
            t = 'git checkout {}'.format(DEV)
            run(t)
            # t = 'git fetch origin {}'.format(DEV)
            # run(t)
            # t = ('git merge --no-ff '
            #      + '-m "merge with on-ff" {}/{}').format(ORIGIN, DEV)
            t = 'git pull {} {} {}'.format(ORIGIN, DEV, DEV)
            run(t)
        return None

    def docker_log(self, container_name, *args, **kw):
        """查看远程的docker log
        """
        with cd(REMOTE_PATH):
            t = 'docker logs -f --tail 50 {}'.format(container_name)
            run(t)
        return None

    def docker_restart(self, container_name, *args, **kw):
        """重启远程container
        """
        cfg = {
            CONTAINER_DEV: self._docker_compose_restart,
            CONTAINER_DEV_CELERY: self._docker_compose_restart_celery,
        }
        if container_name not in cfg:
            t = '容器重启失败: {}'.format(container_name)
            print(t)
            return None
        f = cfg[container_name]
        f()
        return None

    def docker_bash(self, container_name, *args, **kw):
        """进入远程container bash
        """
        with cd(REMOTE_PATH):
            t = 'docker exec -it {} bash'.format(container_name)
            run(t)
        return None

    def docker_update_image(self, container_name, *args, **kw):
        """docker images 推送到aliyun仓库, 然后在服务器下拉, 且重启容器.
        """
        # docker login
        t = 'sudo docker login --username={} --password={} {}'.format(
            USER, PW, PUBLIC
        )
        local(t)
        # 推送镜像
        t = 'sudo docker push {}/{}/{}:{}'.format(
            PUBLIC, NAMESPACE, IMAGENAME, IMAGE_VERSION
        )
        local(t)

        # # 服务器docker login
        # t = 'docker login --username={} --password={} {}'.format(
        #     USER, PW, PUBLIC
        # )
        # run(t)
        # # 下拉镜像
        # t = 'docker pull {}/{}/{}:{}'.format(
        #     PUBLIC, NAMESPACE, IMAGENAME, IMAGE_VERSION
        # )
        # run(t)
        # # 更新容器
        # cfg = {
        #     CONTAINER_DEV: self._docker_compose_up,
        #     CONTAINER_DEV_CELERY: self._docker_compose_up_celery,
        # }
        # if container_name not in cfg:
        #     t = '容器更新失败: {}'.format(container_name)
        #     print(t)
        #     return None
        # f = cfg[container_name]
        # f()
        return None

    def _docker_compose_up(self, *args, **kw):
        with cd(REMOTE_PATH):
            t = 'docker-compose up -d'
            run(t)
        return None

    def _docker_compose_up_celery(self, *args, **kw):
        with cd(REMOTE_PATH):
            t = 'docker-compose -f {}.yml up -d'.format(COMPOSE_NAME_CELERY)
            run(t)
        return None

    def _docker_compose_restart(self, *args, **kw):
        with cd(REMOTE_PATH):
            t = 'docker-compose restart'
            run(t)
        return None

    def _docker_compose_restart_celery(self, *args, **kw):
        with cd(REMOTE_PATH):
            t = 'docker-compose -f {}.yml restart'.format(COMPOSE_NAME_CELERY)
            run(t)
        return None
