PostgreSql 数据库的备份与恢复  
=

参考文章:  

* 章 25. 备份和恢复 http://www.postgres.cn/docs/9.6/backup-dump.html#BACKUP-DUMP-RESTORE  

* pg_dump 的使用 http://www.postgres.cn/docs/9.6/app-pgdump.html  

* psql 的使用 http://www.postgres.cn/docs/9.6/app-psql.html  

备份数据库:  

* 生成备份文件  
  `pg_dump -U database_username -h 127.0.0.1 -d databasename > backupfilename.dmp`  
  必须指定数据库用户, 服务器地址和数据库名.  

* 数据恢复之前, 必须自行创建数据库, 数据用户和赋予相应的权限, 完成之后再进行数据恢复.  
  `psql -U database_username -h 127.0.0.1 -d databasename < backupfilename.dmp`  

* 用指定的数据库用户登录数据库.  
  `psql -U database_username -h 127.0.0.1 -d databasename`  
