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

3. python 包, 互相载入的问题.  
   * 项目结构:
     * myproject/  
       * app_main.py  
       * data/ 
         * \__init__.py 
         * save.py
         * utils/  
           * \__init__.py
           * tools.py  
       * api_func/  
         * \__init__.py 
         * handle.py  

   * 操作方式:  
     1. tools.py 里载入 save.py:  
        `from ..save import xxx`  
        这里 `..` 表示上一级菜单
     2. tools.py 里载入 app_main.py:  
        `from app_main import xxx`  
        如果要引用其他包, 则默认从顶包的目录作为起点    
     3. tools.py 载入 handle.py:  
        `from api_func.handle import xxx`  
        道理同上.  
   * 验证, 如何来验证是否成功载入相应的模块呢?, 方法如下:  
     * 用 IDE 的 `引用跳转` 功能, 检测载入情况.  
       在 **vscode** 下, 按住 Ctil 鼠标悬停到模块上, 出现模块信息, 则  
       成功引用. 点击, 则打开模块所在文件.  

