cytoscape构建复杂网络的数据分析画图软件
=  

[官方下载地址 http://www.cytoscape.org/download.php](http://www.cytoscape.org/download.php)  

参考文章:  

* [http://www.360doc.com/content/17/0305/22/19913717_634279918.shtml](http://www.360doc.com/content/17/0305/22/19913717_634279918.shtml)  

* [http://www.sohu.com/a/136756331_465960](http://www.sohu.com/a/136756331_465960)  

示例讲解:

1. test.xls

        /       A   B
            +++++++++
        1   +   a   b
        2   +   a   c
        3   +   b   c

2. 打开cytoscape->import->network->选择test.xls
3. 在弹出的窗口中去掉first column做为index的勾.
4. 将点击column1, 设置为source.(a a b这一列的header).
5. 点击column2, 设置为target.(b c c这一列的header)
6. 生成network, 即可看见复杂网络图