在 python 中使用 redis  
=  

[redis github](https://github.com/andymccurdy/redis-py)  

1. 主要使用 redis 的队列. 主要命令:  
   
        # 创建实例
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        r = redis.Redis(connection_pool=pool)

        # 队列中加入 {'key': value}
        r.lpush('key', value)

        # 打印队列从0位置到-1位置所有的值, [{'key': value},]
        r.lrange('key', 0, -1)

        # 从队列中最开始的位置取出 key为'key'的值 ('key', value)
        # [1] 表示只返回 ('key', value) 中的 value
        # 0 表示持续监听队列, 如果换成 1 2 3 4 表示监听多少秒
        r.blpop('key', 0)[1]  

   * [参考文章](http://www.jb51.net/article/86021.htm)
