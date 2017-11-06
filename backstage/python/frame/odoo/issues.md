关于 odoo 开发入门可能会遇到的问题
=  

1. 从git克隆的时候使用 --depth=1 的深度比较合适.  

2. 使用 `python odoo-bin -s` 在用户根目录产生 **.odoorc** 文件,  
   此文件可以作为**配置文件**使用, 可改名为 **odoo.conf** 或 **odoo.cfg**.  
   odoo 启动命令 `python odoo-bin -c odoo.conf/cfg`  

3. **action函数**有问题时, 可以尝试重置数据库.  

4. 创建视图时, **tree** 一定要在第一位, 否则无法看见**数据库的全部信息**  
   以及**搜索**.  
   正确设置: `view_mode="tree, form"`  
   吐槽 odoo **v11.0** 官网的 **build module** 教程简直是烂.  

5. 非 admin 用户, 想要看见其他 module 的菜单, 需要配置 security 中的  
   **ir.model.access.csv** 文件.  
   此外, 在上面文件的基础商创建 access rules, 以配置展示信息的规则.  
