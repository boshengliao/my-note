jupyter notebook安装和简介
=  

* 命令行安装`pip install jupyter`  
* 命令行运行`jupyter notebook`  
* 随后会自动在浏览器打开编辑器, 即可进行开发  
* [参考文章](http://blog.csdn.net/lee_j_r/article/details/52791228)  
* 修改jupyter默认目录:  
  * [参考文章](http://blog.csdn.net/tina_ttl/article/details/51031113)  
  * 在`jupyter_notebook_config.py`中修改默认dir  

        # The directory to use for notebooks and kernels.  
        c.NotebookApp.notebook_dir = u'/your/jupyter/work/dir'  

  * 输入`jupyter notebook --generate-config`  
    查看**jupyter_notebook_config.py**所在的位置