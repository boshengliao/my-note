大批量数据导入postegresql
=  

[参考文章](http://blog.csdn.net/colourless/article/details/41444069)  

**重点内容:**  
* 批量导入函数`cursor.executemany(sql, params)`  
  sql为数据库语句, 例: `INSERT INTO 表名 VALUES (%s, %s...)`  
  params为`list`, list中的一个元素(`list/tuple`)为一组数据,  
  例: params = `[(a, b, c), (a, b, c)]`或者`[[a, b, c], [a, b, c]]`  
* 只在数据插入**前**, **后**访问数据库. 在数据生成循环中访问数据库会造成  
  效率极其低.