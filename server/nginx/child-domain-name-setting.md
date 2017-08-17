Nginx 子域名访问设置  
=  

设置如下:  
1. 假设域名 your.dev.com, 绑定在ip: 110.10.110.110 上.  
2. 一般的设置, 只能通过 your.dev.com 访问到一个项目, 实例如下:  

        server {  
            listen 80;
            # 此处填写你的域名
            server_name your.dev.com;
            access_log /var/log/nginx/your.log;

            location / {
                # 填写你的项目地址和端口号
                proxy_pass http://your.app:port;
                proxy_http_version 1.1;  

                # 一般请求用下面两条
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  

                # 长连接加上这两条  
                # proxy_set_header Upgrade $http_upgrade;
                # proxy_set_header Connection "upgrade";
            }

            location / {
                root /your/static/;
            }
        }

3. 此时, 需求改变, 你手头有两个项目, app1和app2, 但是只有一个域名
   your.dev.com, 此时可以进行如下设置, 就可以通过`域名/app1/`和`域名/app2/`
   分别对 app1 和 app2 进行访问了.

        server {  
            listen 80;
            # 此处填写你的域名
            server_name your.dev.com;
            access_log /var/log/nginx/your.log;

            # 此处指令写成 /app1/ , 实际为 your.dev.com/app1/
            # 此时, 在浏览器输入 /app1 则会自动补全为 /app1/
            # 反之, 指令写成 /app1 , 则只能访问 your.dev.com/app1
            # 访问 your.dev.com/app1/ 会报错 404
            location /app1/ {
                # 填写 app1 地址和端口号, 结尾处根据实际情况, 选择是否加反斜线 "/"
                proxy_pass http://your.app1:port;
                proxy_http_version 1.1;  

                # 一般请求用下面两条
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  

                # 长连接加上这两条  
                # proxy_set_header Upgrade $http_upgrade;
                # proxy_set_header Connection "upgrade";
            }

            location /app2/ {
                # 填写 app2 地址和端口号
                proxy_pass http://your.app2:port;
                proxy_http_version 1.1;  

                # 一般请求用下面两条
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  

                # 长连接加上这两条  
                # proxy_set_header Upgrade $http_upgrade;
                # proxy_set_header Connection "upgrade";
            }

            location / {
                root /your/static/;
            }
        }