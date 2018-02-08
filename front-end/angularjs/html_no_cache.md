让 angularjs 的路由每次都读取最新的 html
=  

[参考 https://stackoverflow.com/questions/24577945/angularjs-directive-templateurl-doesnt-update/24578333#24578333](https://stackoverflow.com/questions/24577945/angularjs-directive-templateurl-doesnt-update/24578333#24578333)

代码:  

    templateUrl: function() {
        return 'partials/app-mainsec.html?' + new Date();
    }

* 方法2:
  [参考 http://blog.csdn.net/u010039979/article/details/54376856](http://blog.csdn.net/u010039979/article/details/54376856)  

  代码:  

        app.config(['$httpProvider', '...'], function($httpProvider, ...){
            var theHeaders = $httpProvider.defaults.headers
            if (!theHeaders.get) {
                theHeaders.get = {}
            }
            else {
                theHeaders.common['X-Requested-With'] = 'XMLHttpRequest'
                theHeaders.get['Cache-Control'] = 'no-cache'
                theHeaders.get['Pragma'] = 'no-cache'
            }

            ...
        })
