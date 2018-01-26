自动化更新 js 文件  
=

说明:  
因为在生产环境中的项目会在版本迭代的时候, 对页面进行修改和调整, 如果按常规  
的 js 文件载入, 客户的浏览器只会读取本地缓存的旧版本 js.  

常规 js 的载入:  

    <script type="text/javascript" src="test.js"></script>  

为了解决客户能在打开浏览器的第一时间获取最新的 js 文件, 有了如下的方法:  

1. index.html  

        <!DOCTYPE>
        <html>
            <head>
                <p>i am head yoo.</p>
            </head>
            <body>
                <p>i am body...</p>
                
                <script>
                    // 将 console.log 方法, 绑定到 log
                    let log = console.log.bind(console)

                    // 为了让浏览器不缓存 config.js, 在文件名后加上了 ?version=timestamp
                    // 这样每次读取 index.html 时, 浏览器都会从服务器下载最新的 config.js
                    let value = 'config.js?version=' + new Date().getTime()
                    let t = '<script type="text/javascript" src="'+value+'"><\/script>'

                    // 载入 config.js
                    document.write(t)
                </script>
            </body>
        </html>

2. config.js  

        // 设置 js 文件的版本
        let version = 'v2.0'

        // 需要载入的所有 js 文件地址
        let files = [
            'filename0.js',
            'filename1.js',
        ]

        // 加载 files 里的所有 js 文件
        // 为所有的 js 文件标记统一的版本
        // 生成环境的项目每次进行版本迭代时, 更改 version 的值,
        // 客户就能第一时间获取最新的 js 文件
        for (let i in files){
            let value = files[i] + '?version=' + version.toString()
            let t = '<script type="text/javascript" src="'+value+'"><\/script>'
            document.write(t)
        }