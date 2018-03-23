# 动态载入包的函数 __import__()  

在用python Web开发的过程中, 难免会想动态的根据str来载入相应的模块, 这个时候就可以用到ptyhon的内置函数`__import__()`.  
* 使用方法:  

        lib_str = 'top_lib.sub_lib.lib_name.ClassName'
        lib_path, class_name = lib_str.rsplit('.', 1)
        lib_ = __import__(lib_path, fromlist=class_name)
        class_ = getattr(lib_, class_name)
        instance = class_()

  解释:  
  1. lib_str 为web项目从根目录开始到需要载入的目标类/函数的完整路径.  
  2. lib_path 为从项目根目录到待载入类/函数所在的`lib_name.py`文件的路径.  
  3. class_name 为待载入的类/函数.  
  4. lib_ 为载入的项目模块. 相当于 `import lib_`.
  5. class_ 为类/函数名.