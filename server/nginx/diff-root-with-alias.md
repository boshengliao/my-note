关于 nginx 指令中 root 和 alias 的区别
=  

转自: [http://www.cnblogs.com/tintin1926/archive/2012/07/11/2586813.html](http://www.cnblogs.com/tintin1926/archive/2012/07/11/2586813.html)  

区别如下:  

        location /img/ {
            alias /var/www/image/;
        }
        #若按照上述配置的话，则访问/img/目录里面的文件时，ningx会自动去/var/www/image/目录找文件
        location /img/ {
            root /var/www/image;
        }
        #若按照这种配置的话，则访问/img/目录下的文件时，nginx会去/var/www/image/img/目录下找文件。]