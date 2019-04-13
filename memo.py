#!/usr/bin/python3


# memo
from datetime import datetime as date
import os, sys


# user書き換えて
path = '/home/user/Desktop/memo/'
filename = 'memo.' + date.now().strftime('%Y%m%d')


# メモディレクトリがあったらメモ新規か追記
# なかった場合はディレクトリを作成して新規
while True:
    if os.path.exists(path):
        if os.path.isfile(path + filename):
            memo = open(path + filename, 'a')
            break
        else:
            memo = open(path + filename, 'w')
            break
    else:
        os.mkdir(path)


# 引数にメモの内容を書く
memo.write(' '.join(sys.argv[1:]) + '\n')
memo.close()
