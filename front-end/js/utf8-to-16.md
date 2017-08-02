js中遇到编码问题
=  

* 例子: `var t = '\xe4\xb8\x8a\xe6\xb5\xb7\xe5\xb8\x82'`在js中,  
  即使设置了`charset="utf-8"`  
  依旧会显示乱码.  
* 解决方案: [参考文章](http://shihuan830619.iteye.com/blog/1828235)  
* 其中利用了一个函数`utf8to16(str)`来转换了编码的问题.  

      function utf8to16(str) {  
        var out, i, len, c;  
        var char2, char3;  

        out = "";  
        len = str.length;  
        i = 0;  
        while(i < len) {  
            c = str.charCodeAt(i++);  
            switch(c >> 4)  
            {   
            case 0: case 1: case 2: case 3: case 4: case 5: case 6: case 7:  
                out += str.charAt(i-1);  
                break;  
            case 12: case 13:  
                char2 = str.charCodeAt(i++);  
                out += String.fromCharCode(((c & 0x1F) << 6) | (char2 & 0x3F));  
                break;  
            case 14:  
                char2 = str.charCodeAt(i++);  
                char3 = str.charCodeAt(i++);  
                out += String.fromCharCode(((c & 0x0F) << 12) |  
                    ((char2 & 0x3F) << 6) |  
                    ((char3 & 0x3F) << 0));  
                break;  
            }  
        }  
        return out;  
      }  

* 正确赋值姿势: `var t = utf8to16(unescape("\xe4\xb8\x8a\xe6\xb5\xb7\xe5\xb8\x82"))`  
  输出信息: `上海市`