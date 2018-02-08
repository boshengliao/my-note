让 angularjs 的路由每次都读取最新的 html
=  

[参考 https://stackoverflow.com/questions/24577945/angularjs-directive-templateurl-doesnt-update/24578333#24578333](https://stackoverflow.com/questions/24577945/angularjs-directive-templateurl-doesnt-update/24578333#24578333)

代码:  

    templateUrl: function() {
        return 'partials/app-mainsec.html?' + new Date();
    }
