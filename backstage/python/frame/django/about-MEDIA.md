关于 django 中如何使用 MEDIA
=  

在 django 的学习中, 发现静态文件有两种, 通常页面的插件, 背景图片等都是 STATIC.  
而上传的静态文件, 如: 头像, 资料等, 则被划分为 MEDIA.  

* 关于静态文件, 在 django setting.py 中有 4 个变量, 分别是:  
  1. STATIC_URL  
  2. STATIC_ROOT  
  3. MEDIA_URL  
  4. MEDIA_ROOT  

* 此外, 还有一个定义 setting.py 所在项目的绝对路径.  
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  

* 通常 `STATIC_URL = '/static/'` , 当 **Debug = True** 时, 作为**访问**静态资源**请求**的**前缀**, 会  
  遍历所有 app 下的static 文件夹, 并返回找到第一匹配的文件.  

* 通常 `STATIC_ROOT = os.path.join(BASE_DIR, '../static/'）`, 用于部署应用时存放收集的静态文件,  
  django 的收集命令 `python manage.py collectstatic`, django 会将所有 app 下的 static 文件放置  
  在 STATIC_ROOT 下.  

* 通常 `MEDIA_ROOT = BASE_DIR + '/app_or_project/media/'`, 用户存放上传的文件. 且为**绝对路径**.

* 通常 `MEDIA_URL = '/media/'`, 当 **Debug = True** 时, 作为**访问**静态资源**请求**的**前缀**, 会  
  遍历 MEDIA_ROOT 中 ../media/ 下的文件夹或文件, 并返回找到第一匹配的文件.  
  且需要在**项目**的 `urls.py` 中加入**配置代码**:  

        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            ...
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  以上代码仅在 **Debug = True** 时有效果.  

  关于 STATIC 也可以类似配置, 但是 django 已经**自带**了.  
  
  若你打算在模版中使用 {{ MEDIA_URL }} , 那么应在TEMPLATES的'context_processors'设置中  
  添加'django.template.context_processors.media'.
