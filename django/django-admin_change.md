# 設定管理後台
### 將django Admin加入`INSTALLED_APPS`
- 後台管理的功能django預設為開啟，可以從文件mysite/settings.py查看
```bash
# mysite/settings.py

INSTALLED_APPS = (
    'django.contrib.admin',
    ...
)
```
### 設定管理後台的URL
- 開啟urls.py，新增`path('admin/', admin.site.urls),`
  於urlpatterns內。
```bash
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
]
```
### 建立superuser
> python3 manage.py createsuperuser

### 註冊Model class
- 讓django知道有哪些model需要管理後台
- 修改trips app裡面的admin.py並註冊Post這個Model
> vi trips/admin.py
```bash
# trips/admin.py

from django.contrib import admin
from .models import Post


admin.site.register(Post)
```

> PS: django通常以Post object來表示Post物件，可以透過修改
      def __str__()來更改表示方式
```bash
# trips/models.py

from django.db import models


class Post(models.Model):
    ...
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```
