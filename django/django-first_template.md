# 紀錄使用django流程
```
1. 使用pip3安裝virtualenv
```
> pip3 install virtualenv
```
2. 使用virtualenv指令創造一個專屬於自己的virtualenv
```
> virtualenv myenv
```
3. 啟用virtualenv下的actvie
```
> source bin/active
```
4. 在virtualenv下安裝django
```
> pip3 isntall django
```
5. 使用環境內的django-admin.py創造一個django專案
```
> django-admin.py startproject mysite
```
6. 至此已經完成一個django專案，可以透過進入mysite執行manage.py來確認
   成功會於http://127.0.0.1:8000看到成功畫面
```
> cd mysite && python3 manage.py runserver


# 建立第一個django的app
```bash
1. 使用startapp來創建第一個app 'trips'
```
> python3 manage.py startapp trips
```bash
2. 新增app 'trips'的設定檔
   1. 打開mysite嚇得設定檔settings.py
```
> vi mysite/settings.py
```bash
   2. 找到INSTALLED_APPS變數，並在變數內加入trips，如下
```
>  mysite/settings.py
> 
> ...
>
> INSTALLED_APPS = (
     'django.contrib.admin',
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
     'trips',
> )

# django網頁運作流程Views and URLconfs
- 一般網頁操作流程:
> 瀏覽器送出HTTP request，Django依據URL configuration分配至對應的View；
> View進行資料庫的操作或其他運算，回傳HTTPResponse後由瀏覽器顯示網頁畫面。

## 編輯第一個django Views
```bash
- view的主要功用為在收到HTTPRequest時候要回傳HTTPRespons
  1. 進入之前建立好的app 'trips'並且編輯裡面的views.py
     使用django.http的函數HTTPResponse。將以下代碼貼入；
     # trips/views.py
    from django.http import HttpResponse

    def hello_world(request):
        return HttpResponse("Hello World!")
```
> vi trips/view.py
> ...

## 設定django URL(設定endpoint)
> vi mysite/urls.py
> ...
```
編輯設定urls.py
如果有人瀏覽http://127.0.0.1:8000/hello/時，
hello_world()這個view function會被執行。
  1. 打開mysite/urls
  2. import 剛剛改寫過的views
  3. 添加url(r'^hello/$', hello_world),到urlpatterns
     檔案文件內容如下;
        from django.contrib import admin
        # from django.urls import path
        from django.conf.urls import url
        from trips.views import hello_world

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('hello/', hello_world),
        #    url(r'^hello/$', hello_world),   # another method which needs to import django.urls.path
        ]
```

# 建置第一個Template
- 建置此資料夾目的為將前端程式碼獨立出來，放在templates資料夾內，
  不僅可以增加程式可讀性。也方便設計師及前端工程師的分工。
- 建置一個Template資料夾(與manage.py同一層)
> mkdir templates
- 命名一個templates.py的檔案。
- 設定templates資料夾的位置。將'DIRS'原本的[]改成
  [os.path.join(BASE_DIR, 'templates').replace('\\', '/')]
> vi mysite/setting/py
> ...
```bash
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
# 建立第一個Template，新增一個hello_world.html
- 在templates資料夾內新增一個hello_world.html
```bash
<!-- hello_world.html -->

<!DOCTYPE html>
<html>
    <head>
        <title>I come from template!!</title>
        <style>
            body {
               background-color: lightyellow;
            }
            em {
                color: LightSeaGreen;
            }
        </style>
    </head>
    <body>
        <h1>Hello World!</h1>
        <em>{{ current_time }}</em>
    </body>
</html>
```

- 修改原始hello_world的views
- 使用render function修改回傳物件，修改如下。
```bash
# trips/views.py

from datetime import datetime
from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })
```
