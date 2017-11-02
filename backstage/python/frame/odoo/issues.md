关于 odoo 开发入门可能会遇到的问题
=  

1. 从git克隆的时候使用 --depth=1 的深度比较合适.  

2. 使用 `python odoo-bin -s` 在用户根目录产生 **.odoorc** 文件,  
   此文件可以作为**配置文件**使用, 可改名为 **odoo.conf** 或 **odoo.cfg**.  
   odoo 启动命令 `python odoo-bin -c odoo.conf/cfg`  

3. **action函数**有问题时, 可以尝试重置数据库.  