js中遇到编码问题
=  

* 例子: `var t = '\xe4\xb8\x8a\xe6\xb5\xb7\xe5\xb8\x82'`在js中,  
  即使设置了`charset="utf-8"`  
  依旧会显示乱码.  
* 解决方案: [参考文章](http://shihuan830619.iteye.com/blog/1828235)  
  其中利用了一个函数`utf8to16(str)`来转换了编码的问题.  
  最后重新赋值则可以正常显示. 
* 正确赋值姿势: `var t = utf8to16(unescape("\xe4\xb8\x8a\xe6\xb5\xb7\xe5\xb8\x82"))`  
  输出信息: `上海市`