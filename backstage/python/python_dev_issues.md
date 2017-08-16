记录使用 Python 进行开发时遇到的问题
=  

issues:  

1. 生成的一个 `list` 是唯一的, 不能重复使用. 否则, 赋值会被覆盖.  
   * 用 `id(list)` 可查看唯一的id  
   * 被覆盖的情况:  
   
         a = [1, 2, 3]
         b = a
         c = b
         a[0] = 2
         print a
         print b
         print c
         # 输出 a: [2, 2, 3]
         # 输出 b: [2, 2, 3]
         # 输出 c: [2, 2, 3]

         # 类似下面情况也一样会被覆盖
         a = [1, 2, 3]
         b = a * 3
         a[0] = 2
         # 输出 b: [2, 2, 3, 2, 2, 3, 2, 2, 3]

2. 函数接收到的 JSON 数据为 unicode 编码, 不能正常使用 key 读取数据.  
   * 使用 `pip install pyyaml`  
     
         import yaml  

         # json_datas = json.dumps(datas) 
         # 此时 normal_datas 为正常 utf-8 编码
         normal_datas = yaml.safe_load(json_datas)  