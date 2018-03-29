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

2. 我的**log_cfg.py**:  

        #!/usr/bin/env python
        # -*- coding: utf-8 -*-

        from __future__ import unicode_literals

        import datetime
        import logging

        # 输入log等级, 可填入DEBUG, INFO, WARNING, ERROR, CRITICAL
        logging.basicConfig(level=logging.ERROR)


        def log(message, level='info'):
            """打印 log 信息.

            :param message: 需要打印的信息.  
            :param level: 打印信息的等级. 可填入:
                'debug', 'info', 'warning', 'error', 'critical'.
            """
            # 检查
            cfg = ['debug', 'info', 'warning', 'error', 'critical']
            if level not in cfg:
                level = 'info'
            t = datetime.datetime.now()
            date_time = t.strftime('%Y-%m-%d %H:%M:%S')
            msg = '{}: {}'.format(date_time, message)
            # get func
            f = getattr(logging, level)
            f(msg)
            return None
