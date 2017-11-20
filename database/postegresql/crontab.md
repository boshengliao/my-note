关于定时备份数据库  
=  

* 参考: http://blog.csdn.net/neosmith/article/details/23431651  

* 参考: http://blog.itpub.net/24349972/viewspace-2131643/  

* 编写脚本文件 backup.sh  

        #!/bin/bash  
    
        cur_time=`date +%Y-%m-%d_%T`  
        pg_dump -U database_username -h 127.0.0.1 -d databasename -w > "/home/username/backup_sql/backup_file_$cur_time.dmp"  
        
        echo "backup finished"  

* **.pgpass** 文件如果是root用户来使用, 则放到 /home/ 下.  
  如果是user来使用, 则放到 /home/user/下.
  
        # .pgpass file content
        # hostname:port:database:username:password  
        127.0.0.1:5432:database:username:pw 

* 当前成功的案例是切换至 root 用户, 在生成/root/.pgpass文件,  
  且改变权限`chmod 0600 /root/.pgpass`.  
  然后在 root 用户下 `crontab -e` 添加定时任务.  
  查看cron运行状态 `service cron status`
