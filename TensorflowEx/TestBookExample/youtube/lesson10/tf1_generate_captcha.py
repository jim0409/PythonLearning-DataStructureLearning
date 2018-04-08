# 驗證碼生成庫
# CAPTCHA ; Completely Automated Public Turing test to tell Computers and Humans Apart
from captcha.image import ImageCaptcha
import numpy as np
from PIL import Image
import random
import sys

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def random_captcha_text(char_set=number, captcha_size=4):
    # 驗證碼列表
    captcha_text = []
    for i in range(captcha_size):
        # 隨機選擇
        c = random.choice(char_set)
        # 加入驗證碼列表
        captcha_text.append(c)
    return captcha_text


# 生成字符對應的驗證碼
def gen_captcha_text_and_image():
    # 預設是產生160*60的圖片
    image = ImageCaptcha()
    # 獲得隨機生成的驗證碼
    captcha_text = random_captcha_text()
    # 把驗證碼列表轉為字串符號
    captcha_text = ''.join(captcha_text)
    # 生成驗證碼
    captcha = image.generate(captcha_text)
    image.write(captcha_text, './captcha/' + captcha_text + '.jpg')  # 寫到文件


# 數量可能會少於10000，因為重名
num = 10000
if __name__ == '__main__':
    for i in range(num):
        gen_captcha_text_and_image()
        sys.stdout.write('\r>> Creating image %d/%d' % (i + 1, num))
        sys.stdout.flush()
    sys.stdout.write('\n')
    sys.stdout.flush()
    print("生成完畢")
