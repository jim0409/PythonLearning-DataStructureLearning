# reference : https: // bbs.csdn.net/topics/392190705

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from bottle import *


HTML = """
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>定義input type="file" 的樣式</title>
    <style type="text/css">
        body {
            font-size: 14px;
            align-text: center;
        }

        input {
            vertical-align: middle;
            margin: 0;
            padding: 0
        }

        .file-box {
            position: relative;
            width: 340px;
            margin: 0px auto;
        }

        .txt {
            height: 22px;
            border: 1px solid #cdcdcd;
            width: 180px;
        }

        .btn {
            background-color: #FFF;
            border: 1px solid #CDCDCD;
            height: 24px;
            width: 70px;
        }

        .file {
            position: absolute;
            top: 0;
            right: 80px;
            height: 24px;
            filter: alpha(opacity:0);
            opacity: 0;
            width: 260px
        }
    </style>
</head>

<body>
    <div class="file-box">
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type='text' name='textfield' id='textfield' class='txt' />
            <input type='button' class='btn' value='瀏覽...' />
            <input type="file" name="fileField" class="file" id="fileField" size="28" onchange="document.getElementById('textfield').value=this.value" />
            <input type="submit" name="submit" class="btn" value="上傳" onclick="" />
        </form>
    </div>
</body>

</html>
"""


base_path = os.path.dirname(os.path.realpath(__file__))  # 獲取腳本路徑

upload_path = os.path.join(base_path, 'upload')   # 上傳文件目錄
if not os.path.exists(upload_path):
    os.makedirs(upload_path)


@route('/', method='GET')
@route('/upload', method='GET')
@route('/index.html', method='GET')
@route('/upload.html', method='GET')
def index():
    """顯示上傳頁面"""
    return HTML


@route('/upload', method='POST')
def do_upload():
    """處理上傳文件"""
    filedata = request.files.get('fileField')

    if filedata.file:
        file_name = os.path.join(upload_path, filedata.filename)
        try:
            filedata.save(file_name)  # 上傳文件寫入
        except IOError:
            return '上傳文件失敗'
        return '上傳文件成功, 文件名: {}'.format(file_name)
    else:
        return '上傳文件失敗'


@route('/favicon.ico', method='GET')
def server_static():
    """處理網站圖標文件，找個圖標文件放在腳本目錄裡"""
    return static_file('favicon.ico', root=base_path)


@error(404)
def error404(error):
    """處理錯誤信息"""
    return '404 發生頁面錯誤，未找到內容'


run(host="0.0.0.0", port=8080, reloader=False)  # reloader設置為True可以在更新代碼時自動重載
