#!/usr/bin/python3


# HTML授業のディレクトリ作成するプログラム
import os
from datetime import datetime


# 作るモノの情報
today = datetime.now().strftime('%Y%m%d')


# 学籍番号
my_number = '自分の学籍番号を入れてね'
user = '{}_{}'.format(my_number, today)
css = 'css'
images = 'images'
css_style = 'style.css'
index = 'index.html'


# css作成
os.makedirs('{}/{}/{}'.format(today, user, css))
cssf = open('{}/{}/{}/{}'.format(today, user, css, css_style), 'w')
contents = '''@charset 'utf-8';'''
cssf.write(contents)
cssf.close()


# imagesの作成
os.makedirs('{}/{}/{}'.format(today, user, images))


# index.htmlの作成
indexf = open('{}/{}/{}'.format(today, user, index), 'w')
contents = '''<!DOCTYPE html>\n<html lang='ja'>\n  <head>\n    <meta charset='utf-8'>\n    <meta name='viewport' content='width=device-width, initial-scale=1'>\n    <link rel='stylesheet' href='css/style.css' type='text/css'>\n    <title>hoge</title>\n  </head>\n  <body>\n    body\n  </body>\n</html>'''
indexf.write(contents)
indexf.close()
