zeppelin简介
=  

这是一款基于java的`在线`数据分析, 作图的应用.  
通过简单的设置, 就可以直接访问数据库, 利用其数据做图表, 十分便利.  

* [zeppelin官网](http://zeppelin.apache.org/)  
* 在zeppelin成功运行后, 到`http://localhost:8080/#/interpreter`  
  下搜索`psql`(这里因为我自己用的是 postegresql 数据库)  
  点击右侧**edit**, 修改:  
  * postgresql.user
  * postgresql.password
  * postgresql.url 默认值为 jdbc:postgresql://localhost:5432/  
    修改为: jdbc:postgresql://localhost:5432/**yourDatabase**  

* 至此, 即可访问数据库  
  
      %psql.sql  
      SELECT * FROM yourtable

* python中的库可以直接在**cell**里引入.  
* 代码能在**cell**里直接运行  
* 能定时执行代码

***  

疑问:  
当前我的本地环境**已经安装**搭好了 saprk , 然后在 zeppelin 启动的网址里,  
不用任何设置, 直接载入模块就行. 这样让我感觉很方便,  
但是如果换成**未搭设**好的 spark 的环境, 那么 spark 能否正常运行呢?