百度echart.js
===  
感觉还不错的可视化的插件, 在使用上遇到了一个大坑, 所以来填了一下.  
* [官网文档 echart 2.2.7](http://echarts.baidu.com/echarts2/doc/doc.html#实例方法)  
* [快速开始实例](http://echarts.baidu.com/echarts2/doc/start.html)  

***
按照上面的方法很快能熟悉怎么使用这个插件, 但是其中有一个**大坑**,  
而且最容易发生在自己**手写**的情况下. 那就是:  

    require(
        [
            'echarts',
            'echarts/bar',
            'echarts/line',
        ]
    )

自己html页面中, require加载路径**必须必须必须**和上面一模一样, 随意修改则不能使用!!!