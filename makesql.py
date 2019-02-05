#!/usr/bin/python3


# 山内sql授業のディレクトリ
import os
from datetime import datetime


# 作るもの情報
today = datetime.now().strftime('%m%d')


# ディレクトリの作成
os.makedirs(today)


# ファイルの作成
for p in range(1, 5 + 1):
    make_file = open('{}/{}.{}.sql'.format(today, today, p), 'w')
    make_file.close()
