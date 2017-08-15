记录在 Flask 开发项目中遇到的一些问题  
=  

issues:  

1. 函数接收到的 JSON 数据为 unicode 编码, 不能正常使用 key 读取数据.  
   * 使用 `pip install pyyaml`  
     
         import yaml  

         # json_datas = json.dumps(datas) 
         # 此时 normal_datas 为正常 utf-8 编码
         normal_datas = yaml.safe_load(json_datas)  

2. 运行项目, `app.run(debug=true)`, 不能处理 POST 请求, 此时链接  
   处于 **pedding** 状态.  
   * 启动命令修改:  
     `app.run(debug=True, threaded=True)`  

