关于python logging的简单使用
==  

参考:　[https://www.cnblogs.com/weiok/p/5592448.html](https://www.cnblogs.com/weiok/p/5592448.html)  
[https://docs.python.org/2/library/logging.html](https://docs.python.org/2/library/logging.html)

1. 我的示例代码:  

        #!/usr/bin/env python
        # -*- coding: utf-8 -*-

        import logging
        logging.basicConfig(filename="config.log",
                            filemode="a",
                            format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
                            level=logging.INFO)

        def tt(param=0):
            if param == 0:
                t = '你好 0'
                logging.info(t)
            elif param == 1:
                t = '我是 1'
                logging.info(t)
            else:
                t = '!!!'
                logging.info(t)

        if __name__ == '__main__':
            tt()

   参数描述:  
    * `filename` 填入的是log文件输入的位置.  
    * `filemode` 填入的是输出方式:  
       1. 'a' 为在原有的基础上追加一行.  
       2. 'w' 为重新创建文件并加入一行.
    * `format` 日志输出的格式.
    * `level` 日志输出的级别.
    * ***重要*** 如果直接配置可能会导致框架logging被替换. 如Flask.  
      因为默认`logging.getLogger('werkzeug')`

2. 我的**log_cfg.py**:  

        #!/usr/bin/env python
        # -*- coding: utf-8 -*-

        import logging
        import os


        class Log(object):
            """配置logging
            """
            def __init__(self, proj_name='analysis_log'):
                # 检查项目log目录
                self._check_proj(proj_name)
                # 配置基础变量
                name = proj_name
                log_name = '{}/{}_error.log'.format(proj_name, proj_name)
                level = logging.INFO
                FORMAT = ('%(asctime)s-%(name)s-%(levelname)s: %(message)s')    
                # 生产logger实例
                logger = logging.getLogger(name)
                # 判断logger是否存在
                t = logger.handlers
                if len(t) != 0:
                    self.logger = logger
                    return None

                formatter = logging.Formatter(FORMAT)
                logger.setLevel(level=level)
                # 构造file
                handler = logging.FileHandler(log_name)
                handler.setLevel(level)
                handler.setFormatter(formatter)
                logger.addHandler(handler)
                # 构造stream
                # console = logging.StreamHandler()
                # console.setLevel(level)
                # console.setFormatter(formatter)
                # logger.addHandler(console)

                self.logger = logger
                return None

            def log(self, message, exc_info=True):
                """输出信息
                """
                self.logger.error(message, exc_info=exc_info)
                return None

            def _check_proj(self, proj_name):
                """检查项目文件夹是否存在. 不存在, 则创建
                """
                t = os.path.exists(proj_name)
                if not t:
                    os.mkdir(proj_name)
                return None

    参考资料:  
    * [https://www.cnblogs.com/liujiacai/p/7804848.html](https://www.cnblogs.com/liujiacai/p/7804848.html)
    * [https://blog.csdn.net/seanb/article/details/52608235](https://blog.csdn.net/seanb/article/details/52608235)