根据中文排序
=  

* 参考: [python 按中文排序](http://blog.csdn.net/xiaobuding007/article/details/78224159)  

* 内容:  
  1. 更新源 `sudo apt-get update`  
  2. 安装中文包 `sudo apt-get install language-pack-zh-hans-base`
  3. 更新?? 不明白 `sudo dpkg-reconfigure locales`
  4. 用法:

            import locale
            t = locale
            t.setlocale(t.LC_COLLATE, 'zh_CN.UTF8')
            cmpd = t.strcoll
            r = sorted(datas, cmp=lambda x, y: cmpd(x[key], y[key]), 
                       reverse=reverse)