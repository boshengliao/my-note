设置mongodb的副本集来实现高可靠/读写分离的服务  
=

* 启动mongo, 并设置副本集名称  
    * 命令行 `mongod -f /etc/mongod.conf --bind_ip 0.0.0.0 --port 27022 --replSet rs0`  
        * `--replSet rs0`很重要, 所有用作构建副本集的mongo服务均需有该参数.  
        * 可在配置文件 mongod.conf 里设置 参数`replication: rs0`是同样效果.  

    * 配置--mongod.conf:

            # mongod.conf

            # for documentation of all options, see:
            #   http://docs.mongodb.org/manual/reference/configuration-options/

            # Where and how to store data.
            storage:
            dbPath: /var/lib/mongodb
            journal:
                enabled: true
            #  engine:
            #  mmapv1:
            #  wiredTiger:

            # where to write logging data.
            systemLog:
            destination: file
            logAppend: true
            path: /var/log/mongodb/mongod.log

            # network interfaces
            net:
            port: 27017
            bindIp: 127.0.0.1


            # how the process runs
            processManagement:
            timeZoneInfo: /usr/share/zoneinfo

            #security:

            #operationProfiling:

            #replication:

            #sharding:

            ## Enterprise-Only Options:

            #auditLog:

            #snmp:


* 初始化副本集  
    * 任意选择进入一个mongo shell, 运行`re.initiate(conf)`  

            conf = {
                "_id": "rs0",
                "members": [
                    {"_id": 0, "host": "ip/hostname:port"},
                    {"_id": 1, "host": "ip/hostname:port"},
                    {"_id": 2, "host": "ip/hostname:port"},
                ],
            }

        * 建议用host用**ip:port**的形式, 因为要确保服务器间能**相互访问**  
        * `re.initiate()`也能初始化, 但是本机的**host**可能会由**数字和字符**的形式出现, 导致其他服务器无法找到此节点. 特别是使用**docker**时, 须特别注意!!  
        * 副本集成功时, 各节点状态应该只能是有一个**PRIMARY**和多个**SECONDARY**.
* 操作节点  
    * `rs.add("ip/hostname:port")`
    * `rs.remove("ip/hostname:port")`  

* 使用 mongoengine 连接副本集:  

        from mongoengine import connect

        ip = '172.17.0.1'
        uri = 'mongodb://{ip}:27020,{ip}:27021,{ip}:27022/test'.format(ip=ip)
        # uri = 'mongodb://{ip}:27020,{ip}:27021,{ip}:27022/test?replicaSet=rs0'.format(ip=ip)
        connect(host=uri, replicaset='rs0')


参考:  
[官网](https://docs.mongodb.com/manual/replication/)  
[mongoDB系列之（二）：mongoDB 副本集](https://www.cnblogs.com/ee900222/p/mongodb_2.html)