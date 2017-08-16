记录在 Flask 开发项目中遇到的一些问题  
=  

issues:  

1. 运行项目, `app.run(debug=true)`, 不能处理 POST 请求, 此时链接  
   处于 **pedding** 状态.  
   * 启动命令修改:  
     `app.run(debug=True, threaded=True)`  

