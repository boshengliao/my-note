配置 ssh config 文件
=  

通过配置 `ssh config`, 可以很方便的访问服务器.  

* [参考文章](https://segmentfault.com/a/1190000000585526)  
  1. 核心命令 `ssh-keygen -t rsa -C "advice.use.your@email" -f my-key-file`  
     * `-t rsa` 是生成密钥的方式, 建议使用 **rsa**
     * `-c "str"` 是添加为密钥**备注信息/标记**, 通常使用自己的邮箱, 可缺省,  
       建议使用自己的**邮箱**  
     * `-f filename` 是指定密钥的文件名, 可缺省  
       缺省, 则生成 **id_rsa** 和 **id_rsa.pub** 两个文件
  2. 本地目录 `~/.ssh/` 下, 生成 `config` 文件, 内容:  
     
         Host mys
             HostName yourip
             User your_username
             IdentityFile ~/.ssh/my-key-file  

  3. 将本地公钥加入到远程服务器, 执行:  
     `ssh-copy-id -i my-key-file.pub mys`  
     * my-key-file.pub 为公钥文件  
     * mys 为 **config** 文件中, Host 的值  
     
     执行过程中会最后一次让你输入服务器的登录密码, 完成之后, 会在服务器**自动**  
     **生成** `~/.ssh/authorized_keys` 且**自动加入**公钥信息.