关于 shadowsocks 的使用  
==  

1. Window 直接下载软件, 配置:  
   * 服务器地址  
   * 端口号  
   * 密码  
   * 直接连接即可, 通常是PCA模式或者全局模式  

2. ubuntu 上, 配置  
   * 安装 `pip install shadowsocks`  
   * 创建文件 `mkdir shadowsocks.json`, 内容为:  

            {
                "server":"服务器的ip",
                "server_port":19175,
                "local_address":"127.0.0.1",
                "local_port":1080,
                "password":"密码",
                "timeout":300,
                "method":"aes-256-cfb",
                "fast_open":false
            }
    
   * 启动代理 `sslocal -c shadowsocks.json`  
   * 使用 google chrome 浏览器安装 [switchysharp](http://www.cnplugins.com/devtool/proxy-switchysharp/)  
     * 新建情景 `ss`  
     * SOCKS Host: `127.0.0.1`  
     * 端口号: `1080`  
     * 选择 `SOCKS v5`  
     * 规则填写 `ss *.google.* wildcard ss`  
     * 在线规则 `https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt`  
     * 选中在线自动代理
     * 更新列表
     * 保存