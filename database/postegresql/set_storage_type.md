指定 Postgresql 数据库的 COLLATE 和 ctype  
=  

参考：  

* PostgreSQL 创建库时如何指定 Collate, Ctype: https://yq.aliyun.com/articles/55713  

* PostgreSQL 创建库时如何指定 Collate, Ctype: http://blog.163.com/digoal@126/blog/static/1638770402016625105728265/  

主要内容:  

* 指定数据的 collate 和 ctype 为**zh_CN.UTF8**格式.  
  `>postgres=# create database tmpdb_zh_cn with template template0 lc_collate 'zh_CN.UTF8' lc_ctype 'zh_CN.UTF8' is_template=true owner username;`