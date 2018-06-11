在win10的基础上安装Ubuntu
=  

[参考文章(含安装、删除、恢复引导)](http://blog.csdn.net/michael_lbs/article/details/63251850)  
[ubuntu引导修复](https://blog.csdn.net/hp_satan/article/details/9331411)  
重点`set prefix`后, 直接 `insmod normol`

安装ubuntu:  
  1. 在[ubuntu官网](https://www.ubuntu.com/download/alternative-downloads)
  选择自己需要的ubuntu版本文件  
  2. 准备好4G以上剩余空间的U盘  
  3. 使用软碟通(UltraISO)将ubuntu系统文件写入U盘
  4. 在win10上按`ctrl+x`, 在磁盘管理器中选择较大的磁盘:
     * 右键压缩卷  
     * 大小设置为50G  
  5. 重启电脑, 选择u盘启动, 进入ubuntu安装界面:  
     * 选择自己喜欢的语言  
     * 安装ubuntu  
     * 选择**不连接**网络, 继续  
     * 选择**不安装**软件, 继续  
     * 选择最后一项, 自己创建、调整分区, 继续  
     * 选择**空闲**的50G, 点击左下的加号, 依次添加:  
       (1) 大小 15G, 主分区, 空间起始位置, Ext 4 文件系统,
           挂载点: /  
       (2) 大小 8G, 用于: 交换空间(swap) (常设置为内存的两倍),
           挂载点: /swap  
       (3) 大小 剩余的所有空间, 主分区, 空间起始位置, Ext 4 文
       件系统, 挂载点: /home  
     * 安装启动引导器: 使用 **默认默认默认**. (这样ubuntu和win10
       共存, 且由ubuntu引导开机启动)  
     * 选择语言, 选择键盘布局  
     * 至此, 安装结束, 重启进入ubuntu的grub引导启动界面  

***  

如果安装失败, 重启仍进入win10系统:  
1. `ctrl+x`进入磁盘管理系统, **依次**选择之前ubuntu的
   三个区右键`删除卷`, 删除的空间会自动合并, 最终再
   次呈**现空闲的50g**  
2. **仔细**上文的**参考文章**  
3. 按上面 **安装ubuntu** 的步骤再走一遍  

***

如果安装成功了, 想删除ubuntu:  
* 可使用**EasyBCD**修复win10引导, [参考文章](http://jingyan.baidu.com/article/642c9d34e371c3644b46f768.html)  

或者:  

1. 使用 `雨林木风`, `老毛桃` 之类的u盘启动软件  
2. 选择进行`PE系统`  
3. 使用`bootice`:  
   * 选择 物理磁盘处理  
   * 选择 win10所在的目标磁盘  
   * 点击 主引导记录  
   * 选择 NT 5.X/6.X MBR, win7~10 选择6.X  
   * 点击 安装/配置  
   * 返回 物理磁盘处理 页面, 点击 分区引导记录  
   * 选择 BOOTMGR  
   * 点击 安装/配置  
   * [参考文章（bootice使用）](http://jingyan.baidu.com/article/4b52d70291e9b4fc5d774b73.html)
4. 保持U盘始终是插入的状态, 重启电脑, 正常启动win10:  
   * 若**启动成功**, 会在进入系统之前安装一些东西, 稍后正
     常进入win10, 此时如果失败, 请多重启几次
   * 若**启动失败**, 请重新第3条开始  
5. 在 win10 下载**EasyBCD**删除多余开机引导  
6. 此时, 可在`磁盘管理`重新将`不需要`的ubuntu磁盘卷再次删除  
7. 右键`空闲空间`, 新建简单卷, 至此, win10能正常访问这50g了  
