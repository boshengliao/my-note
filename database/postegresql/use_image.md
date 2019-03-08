对于使用[postgres官方镜像](https://hub.docker.com/_/postgres)遇到问题的一些总结  
=  

1.  初始化zh_cn.utf8字符集.  
    * 以任意配置用镜像创建容器  
    * 进入容器, 修改文件`vi /etc/locale.gen`  
    * 取消注释**en_US.UTF-8**和**zh_CN.UTF-8**, 保存
    * 重新加载本地字符集`locale-gen`  
    * 以此容器重新初始化的pg数据库则pg_collation里包含**zh_CN.utf8**字符集  
    注: 可以将此容器保存为新的镜像作为基础镜像.

2.  创建支持中文排序的数据库[参考文章](https://yq.aliyun.com/articles/55713)  
