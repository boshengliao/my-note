关于 profile 被该坏, 出现重复登录  
=  

* 描述:  
  ubuntu 进入用户登录页面, 当输入密码回车时, 屏幕一闪又  
到了登录界面, 继续下去会一直重复登录.  

* 解决:  
  在用户登录页面, 按下 **Alt+Ctrl+F1** 进入 shell 模式,  
  1. 输入用户名  
  2. 输入用户密码, 登录
  3. `sudo cp /etc/profile /etc/profile_bak` 备份 profile
  4. `sudo reboot` 重启
  5. 正常登录即可  
  6. 修改 profile_bak 至正确, 最后重命名为 profile