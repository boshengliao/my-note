在使用 ubuntu 14.04 中碰到的一些问题  
=  

1. 软件中心闪退  
   可能出现的状况:  
   * 最明显的就是软件中心无法打开以及闪退.  
   * 或者出现  **E: 软件包 software-center 需要重新安装，但是我无法找到相应的安装文件。**  

   尝试多方解决办法无果, 最后使用如下办法得救:  
   * `sudo rm /var/lib/apt/lists/* -vf`  
   * `sudo apt-get update`  
   
   解决办法出自: [http://blog.csdn.net/u010510350/article/details/59084563](http://blog.csdn.net/u010510350/article/details/59084563)  