关于python logging的简单使用
==  

参考:　[https://www.cnblogs.com/weiok/p/5592448.html](https://www.cnblogs.com/weiok/p/5592448.html)  

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
