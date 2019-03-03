#!/usr/bin/python3


# 郵便番号で住所を出す
import requests, json


# api
def getURL(post_code):
    return 'http://zipcloud.ibsnet.co.jp/api/search?zipcode={}'.format(post_code)


# Jsonを読む
def readJson(url):
    r = requests.get(url)
    data = json.loads(r.text)
    return data


# 情報を取得
def getInfo(data):
    if not (data['results'] == None):
        return [data['results'][0]['zipcode'],
                data['results'][0]['address1'],
                data['results'][0]['address2'],
                data['results'][0]['address3']]
    else:
        return 'Nothing'


# 最終的な表示
def showInfo(info):
    if not (info == 'Nothing'):
        display('郵便番号{}は{}{}{}です.'.format(info[0], info[1], info[2], info[3]))
    else:
        display('その郵便番号は存在しません.')


# 表示
def display(d):
    print(d)


# 実行
if __name__ == '__main__':
    while True:
        try:
            post_code = int(input('郵便番号を入力してください(例1234567): '))
            showInfo(getInfo(readJson(getURL(post_code))))
            break
        except ValueError:
            display('ERROR')
            break
