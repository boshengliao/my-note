解决搜狗输入法在 ubuntu14.04 中遇到的问题
=  

1. 输入法没法调出sogou. 解决:  
   通过下面的两个命令重启搜狗输入法  
   `~$ killall fcitx`  
   `~$ killall sogou-qinpanel`  

2. sogou只有输入框, 不能输入中文.  
   删除配置文件. ubuntu下搜狗的配置文件在 ~/.config下删除这3个文件夹：  
   **SogouPY、SogouPY.users、sogou-qimpanel**
   