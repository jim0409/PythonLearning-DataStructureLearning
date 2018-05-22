# 使用第一個django model

# 查看與修改內建的db
- 此處敘述如何使用django的database
- 修改mysite/settings.py
> vi mysite/settings.py

```bash
# mysite/settings.py

...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

# 修改django models，定義宣告的Post類別
- 編輯mysite/models.py檔，定義Post類別。
> vi mysite/models.py
> ...
```bash
# trips/models.py

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
```

# 同步資料庫
> python3 manage.py makemigrations
# 將models.py內的欄位寫入資料庫
> python3 manage.py migrate