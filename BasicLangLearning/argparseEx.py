# https://docs.python.org.tw/3/howto/argparse.html
import argparse

# 傳送參數進入程式內
parser = argparse.ArgumentParser()

# 依據增加的參數argument個數決定在執行python的時候要放置幾個參數
# e.g. python3 argparseEx.py dat 123
# console:
#   dat
#   123
parser.add_argument("echo", help="echo the string you use here")
parser.add_argument('day',type=int,help='assigned number for day')

args = parser.parse_args()
print(args.echo)
print(args.day)
